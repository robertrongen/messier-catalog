from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import uuid

db = SQLAlchemy()

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {field: getattr(self, field) for field in self.__table__.columns.keys()}

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False, default=str(uuid.uuid4()))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    username = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {field: getattr(self, field) for field in self.__table__.columns.keys()}

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    annotations = db.relationship('Annotation', backref='user_profile', lazy=True)

class Annotation(db.Model):
    __tablename__ = 'annotations'
    id = db.Column(db.Integer, primary_key=True)
    messier_id = db.Column(db.Integer, db.ForeignKey('MessierObjects.Number'), nullable=False)
    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    captured = db.Column(db.Boolean, default=False)
    cap_year = db.Column(db.Integer)
    remarks = db.Column(db.Text)
    planned = db.Column(db.Boolean, default=False)

class MessierObject(db.Model):
    __tablename__ = 'MessierObjects'
    Number = db.Column(db.Integer, primary_key=True)
    Messier = db.Column(db.String)
    NGC = db.Column(db.String, nullable=True)
    Name = db.Column(db.String, nullable=True)
    Type = db.Column(db.String)
    SubType = db.Column(db.String)
    Season = db.Column(db.String)
    Magnitude = db.Column(db.Integer)
    Const = db.Column(db.String)
    ConstEnglish = db.Column(db.String)
    Constellation = db.Column(db.String)
    RA = db.Column(db.String)
    Dec = db.Column(db.String)
    Distance = db.Column(db.Integer)
    Size = db.Column(db.String)
    Discoverer = db.Column(db.String, nullable=True)
    Year = db.Column(db.Integer, nullable=True)
    annotations = db.relationship('Annotation', backref='messier_object', lazy=True)

    def __repr__(self):
        return f'<MessierObject {self.Messier}>'

    def to_dict(self):
        return {field: getattr(self, field) for field in self.__table__.columns.keys()}
