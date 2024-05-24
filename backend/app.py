# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, current_user, utils, login_user
from flask_uploads import UploadSet, configure_uploads, IMAGES
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv
from models import db, MessierObject, User, Role, UserProfile

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SINGLE_HASH'] = 'bcrypt'

app.logger.addHandler(file_handler)

db.init_app(app)
migrate = Migrate(app, db)

if os.getenv('FLASK_ENV') == 'development':
    cors_origin = os.getenv('DEV_CORS_ORIGIN')
else:
    cors_origin = os.getenv('PROD_CORS_ORIGIN')

CORS(app, resources={r"/api/*": {"origins": cors_origin}}, supports_credentials=True)

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/api/auth/login', methods=['OPTIONS', 'POST'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    email = request.json.get('email')
    password = request.json.get('password')
    user = user_datastore.find_user(email=email)
    if user and utils.verify_password(password, user.password):
        login_user(user)
        token = user.get_auth_token()
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401

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
        elif sort_by == 'season':
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
        return jsonify(messier_list)
    except Exception as e:
        app.logger.error(f"Error fetching Messier data: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route works"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
