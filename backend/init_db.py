from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security, utils
from models import db, User, Role, UserProfile, Annotation, MessierObject
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AstroCaps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SINGLE_HASH'] = 'bcrypt'

db.init_app(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

def create_admin():
    with app.app_context():
        db.create_all()
        if not user_datastore.find_user(email='rongen.robert@gmail.com'):
            user = user_datastore.create_user(
                email='rongen.robert@gmail.com',
                password=utils.hash_password('adminpassword'),
                username='roro',
                roles=['admin']
            )
            db.session.commit()

            user_profile = UserProfile(
                user_id=user.id,
                username='roro',
                first_name='Robert',
                last_name='Rongen'
            )
            db.session.add(user_profile)
            db.session.commit()

            # Migrate existing annotations to the admin user
            # migrate_annotations_to_user(user_profile.id)

def migrate_annotations_to_user(user_profile_id):
    with app.app_context():
        annotations = MessierObject.query.filter_by(user_profile_id=None).all()
        for annotation in annotations:
            annotation.user_profile_id = user_profile_id
        db.session.commit()

if __name__ == '__main__':
    create_admin()
