# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
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
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)

# app.debug = True
# toolbar = DebugToolbarExtension(app)
# app.logger.debug(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

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
    
    def to_dict(self):
        return {
            'Messier': self.Messier,
            'NGC': self.NGC,
            'Name': self.Name,
            'Type': self.Type,
            'Season': self.Season,
            'Captured': self.Captured,
            'CapYear': self.CapYear,
            'Magnitude': self.Magnitude,
            'Constellation': self.Constellation,
            'Const': self.Const,
            'Latin': self.Latin,
            'Right Ascension': self.RA,
            'Declination': self.Dec,
            'Distance': self.Distance,
            'Size': self.Size,
            'Discoverer': self.Discoverer,
            'Year': self.Year
        }

@app.route('/api/messier')
def get_all_messier_objects():
    all_objects = MessierObject.query.all()
    sorted_objects = sorted(all_objects, key=lambda x: int(x.Messier[1:]))  # Sorting by numerical part
    messier_list = [obj.to_dict() for obj in sorted_objects]  # Assuming to_dict is properly implemented
    return jsonify(messier_list)

# Routes to Serve Messier Object Data
@app.route('/api/messier/<messier_number>')
def get_messier_object(messier_number):
    obj = MessierObject.query.filter_by(Messier=messier_number).first()
    if obj:
        return jsonify(obj.to_dict())
    else:
        return jsonify({'error': 'Messier object not found'}), 404

@app.route('/')
def hello():
    return "Hello, Astro Caps!"

if __name__ == '__main__':
    app.run(debug=True)
