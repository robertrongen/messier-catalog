# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
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
# Add the handlers to the app's logger
app.logger.addHandler(file_handler)

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)

class MessierObject(db.Model):
    __tablename__ = 'MessierObjects'
    Number = db.Column(db.String, primary_key=True)
    Messier = db.Column(db.String)
    NGC = db.Column(db.String, nullable=True)
    Name = db.Column(db.String, nullable=True)
    Type = db.Column(db.String)
    SubType = db.Column(db.String)
    Season = db.Column(db.String)
    Magnitude = db.Column(db.Float)
    Const = db.Column(db.String)
    ConstEnglish = db.Column(db.String)
    Constellation = db.Column(db.String)
    RA = db.Column(db.String)
    Dec = db.Column(db.String)
    Distance = db.Column(db.Float)
    Size = db.Column(db.String)
    Discoverer = db.Column(db.String, nullable=True)
    Year = db.Column(db.Float, nullable=True)
    Captured = db.Column(db.Integer, nullable=True)
    CapYear = db.Column(db.Integer, nullable=True)
    Remarks = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<MessierObject {self.Messier}>'
    
    def to_dict(self):
        return {field: getattr(self, field) for field in self.__table__.columns.keys()}

@app.route('/api/messier', methods=['GET'])
def get_all_messier_objects():
    try:
        app.logger.debug("Received request for /api/messier")
        sort_by = request.args.get('sort_by', 'number')
        reverse_sort = request.args.get('reverse_sort', 'false').lower() == 'true'
        filter_captured = request.args.get('filter_captured')
        filter_season = request.args.get('filter_season')
        filter_type = request.args.get('filter_type')
        filter_constellation = request.args.get('filter_constellation')

        query = MessierObject.query
        if filter_captured:
            query = query.filter_by(Captured=int(filter_captured))
        if filter_season:
            query = query.filter_by(Season=filter_season)
        if filter_type:
            query = query.filter_by(Type=filter_type)
        if filter_constellation:
            query = query.filter_by(Constellation=filter_constellation)

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
        # app.logger.debug(f"Query: {str(query)}")

        messier_objects = query.all()
        messier_list = [obj.to_dict() for obj in messier_objects]
        app.logger.debug(f"Fetched data: {messier_list}")
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
            db.session.commit()
            return jsonify(obj.to_dict()), 200
        else:
            return jsonify({'error': 'Messier object not found'}), 404

@app.route('/')
def hello():
    return "Hello, Astro Caps!"

if __name__ == '__main__':
    app.run(debug=True)
