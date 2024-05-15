# backend/app.py
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_debugtoolbar import DebugToolbarExtension
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.debug = True
toolbar = DebugToolbarExtension(app)
app.logger.debug(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

class MessierObject(db.Model):
    __tablename__ = 'MessierObjects'
    Messier = db.Column(db.String, primary_key=True)
    NGC = db.Column(db.String)
    Name = db.Column(db.String)
    Type = db.Column(db.String)
    Season = db.Column(db.String)
    Magnitude = db.Column(db.Float)
    Const = db.Column(db.String)
    Constellation = db.Column(db.String)
    Latin = db.Column(db.String)
    RA = db.Column(db.String)
    Dec = db.Column(db.String)
    Distance = db.Column(db.Float)
    Size = db.Column(db.String)
    Discoverer = db.Column(db.String)
    Year = db.Column(db.Float)
    Captured = db.Column(db.Integer)
    CapYear = db.Column(db.Integer)
    def __repr__(self):
        return f'<MessierObject {self.Messier}>'

@app.route('/api/messier')
def get_all_messier_objects():
    app.logger.debug("Starting database query for all Messier objects.")
    all_objects = MessierObject.query.all()
    app.logger.debug(f"Database query complete. Number of objects fetched: {len(all_objects)}")
    if not all_objects:
        app.logger.debug("Query returned no results.")

    messier_list = []
    for obj in all_objects:
        messier_data = {
            'Messier': obj.Messier,
            'NGC': obj.NGC,
            'Name': obj.Name,
            'Type': obj.Type,
            'Season': obj.Season,
            'Captured': obj.Captured,
            'CapYear': obj.CapYear,
            'Magnitude': obj.Magnitude,
            'Constellation': obj.Constellation,
            'Cons': obj.Const,
            'Latin': obj.Latin,
            'Right Ascension': obj.RA,
            'Declination': obj.Dec,
            'Distance': obj.Distance,
            'Size': obj.Size,
            'Discoverer': obj.Discoverer,
            'Year': obj.Year
        }
        messier_list.append(messier_data)
        app.logger.debug(f"Processed object: {messier_data}")
    app.logger.debug("Completed processing all objects.")
    return jsonify(messier_list)

# Routes to Serve Messier Object Data
@app.route('/api/messier/<messier_number>')
def get_messier_object(messier_number):
    obj = MessierObject.query.filter_by(Messier=messier_number).first()
    if obj:
        return {
            'Messier': obj.Messier,
            'NGC': obj.NGC,
            'Name': obj.Name,
            'Type': obj.Type,
            'Season': obj.Season,
            'Captured': obj.Captured,
            'CapYear': obj.CapYear,
            'Magnitude': obj.Magnitude,
            'Constellation': obj.Constellation,
            'Cons': obj.Cons,
            'Latin': obj.Latin,
            'Right Ascension': obj.RA,
            'Declination': obj.Dec,
            'Distance': obj.Distance,
            'Size': obj.Size,
            'Discoverer': obj.Discoverer,
            'Year': obj.Year
        }
    else:
        return {'error': 'Messier object not found'}, 404

@app.route('/')
def hello():
    return "Hello, Astro Caps!"

if __name__ == '__main__':
    app.run(debug=True)
