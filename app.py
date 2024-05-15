from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class MessierObject(db.Model):
    Messier = db.Column(db.String, primary_key=True)
    NGC = db.Column(db.String)
    Type = db.Column(db.String)
    Season = db.Column(db.String)
    Magnitude = db.Column(db.Float)
    Cons = db.Column(db.String)
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
    Name = db.Column(db.String)
    def __repr__(self):
        return f'<MessierObject {self.Messier}>'


# Routes to Serve Messier Object Data
@app.route('/api/messier/<messier_number>')
def get_messier_object(messier_number):
    obj = MessierObject.query.filter_by(messier_number=messier_number).first()
    if obj:
        return {
            'messier_number': obj.messier_number,
            'name': obj.name,
            'constellation': obj.constellation,
            'right_ascension': obj.right_ascension,
            'declination': obj.declination,
            'magnitude': obj.magnitude,
            'distance': obj.distance,
            'description': obj.description,
            'type': obj.type
        }
    else:
        return {'error': 'Messier object not found'}, 404

@app.route('/')
def hello():
    return "Hello, Astro Caps!"

if __name__ == '__main__':
    app.run(debug=True)
