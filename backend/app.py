# backend/app.py
from models import db, MessierObject
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore, auth_required, roles_required
# from flask_uploads import UploadSet, configure_uploads, IMAGES
import requests  # Import requests module
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Create a file handler and set level to debug
file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)
file_handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
# Add the handlers to the app's logger
app.logger.addHandler(file_handler)

# Initialize extensions
db.init_app(app)  # Properly initialize the db with the app
CORS(app)
migrate = Migrate(app, db)

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

@app.route('/api/messier', methods=['GET'])
def get_all_messier_objects():
    try:
        sort_by = request.args.get('sort_by', 'number')
        reverse_sort = request.args.get('reverse_sort', 'false').lower() == 'true'
        filter_captured = request.args.get('filter_captured')
        filter_season = request.args.get('filter_season')
        filter_type = request.args.get('filter_type')
        filter_constellation = request.args.get('filter_constellation')
        filter_planned = request.args.get('filter_planned')

        query = MessierObject.query
        if filter_captured:
            query = query.filter_by(Captured=int(filter_captured))
        if filter_season:
            query = query.filter_by(Season=filter_season)
        if filter_type:
            query = query.filter_by(Type=filter_type)
        if filter_constellation:
            query = query.filter_by(Constellation=filter_constellation)
        if filter_planned:
            query = query.filter_by(Planned=int(filter_planned))

        if sort_by == 'number':
            order = MessierObject.Number
        if sort_by == 'season':
            order = MessierObject.Season
        elif sort_by == 'type':
            order = MessierObject.Type
        elif sort_by == 'magnitude':
            order = MessierObject.Magnitude
        elif sort_by == 'dec':
            order = MessierObject.Dec
        else:
            order = MessierObject.Number

        if reverse_sort:
            order = order.desc()
        else:
            order = order.asc()

        query = query.order_by(order)

        messier_objects = query.all()
        messier_list = [obj.to_dict() for obj in messier_objects]
        # summary = messier_list[:3]  # Get the first 3 items for summary
        # app.logger.debug(f"Fetched {len(messier_list)} Messier objects. Summary: {summary}")
        return jsonify(messier_list)
    except Exception as e:
        app.logger.error(f"Error fetching Messier data: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/api/messier/<messier_number>')
def get_messier_object(messier_number):
    obj = MessierObject.query.filter_by(Messier=messier_number).first()
    if obj:
        data = obj.to_dict()
        wikipedia_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{obj.Name}"
        response = requests.get(wikipedia_url)
        if response.status_code == 200:
            wiki_data = response.json()
            data['wikipedia'] = wiki_data
        return jsonify(data)
    else:
        return jsonify({'error': 'Messier object not found'}), 404

@app.route('/api/messier/<messier_number>', methods=['GET', 'POST'])
def get_or_update_messier_object(messier_number):
    if request.method == 'GET':
        obj = MessierObject.query.filter_by(Messier=messier_number).first()
        if obj:
            data = obj.to_dict()
            wikipedia_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{obj.Name}"
            response = requests.get(wikipedia_url)
            if response.status_code == 200:
                wiki_data = response.json()
                data['wikipedia'] = wiki_data
            return jsonify(data)
        else:
            return jsonify({'error': 'Messier object not found'}), 404
    elif request.method == 'POST':
        data = request.json
        obj = MessierObject.query.filter_by(Messier=messier_number).first()
        if obj:
            obj.Captured = data.get('Captured', obj.Captured)
            obj.CapYear = data.get('CapYear', obj.CapYear)
            obj.Remarks = data.get('Content', obj.Remarks)
            obj.Planned = data.get('Planned', obj.Planned)
            db.session.commit()
            return jsonify(obj.to_dict()), 200
        else:
            return jsonify({'error': 'Messier object not found'}), 404

@app.route('/api/test', methods=['GET'])
def test_route():
    try:
        app.logger.debug("Received request for /api/test")
        return jsonify({"message": "Test route works"})
    except Exception as e:
        app.logger.error(f"Error fetching test data: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/')
def hello():
    return "Welcome to the interactive deepsky messier catalog!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
