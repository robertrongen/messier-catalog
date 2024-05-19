# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests  # Import requests module
# import logging
# from flask_debugtoolbar import DebugToolbarExtension
import os
from dotenv import load_dotenv

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)

# app.debug = True
# toolbar = DebugToolbarExtension(app)
# app.logger.debug(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

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
    sort_by = request.args.get('sort_by', 'number')
    filter_captured = request.args.get('filter_captured')

    query = MessierObject.query

    if filter_captured is not None:
        query = query.filter_by(Captured=int(filter_captured))

    if sort_by == 'number':
        query = query.order_by(MessierObject.Number.asc())
    elif sort_by == 'season':
        query = query.order_by(MessierObject.Season.asc())
    elif sort_by == 'type':
        query = query.order_by(MessierObject.Type.asc())
    elif sort_by == 'magnitude':
        query = query.order_by(MessierObject.Magnitude.asc())
    else:
        query = query.order_by(MessierObject.Number.asc())

    messier_objects = query.all()
    messier_list = [obj.to_dict() for obj in messier_objects]
    return jsonify(messier_list)

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
