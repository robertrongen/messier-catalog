# backend/models.py
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
# from sqlalchemy.orm import relationship
# from flask_security import UserMixin, RoleMixin
# from sqlalchemy.orm import relationship

db = SQLAlchemy()

# roles_users = db.Table('roles_users',
#     db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#     db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
# )

# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     confirmed_at = db.Column(db.DateTime())
#     roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# class UserProfile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
#     username = db.Column(db.String(50), nullable=False)
#     user = db.relationship('User', backref=db.backref('profile', uselist=False))
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)

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
    Captured = db.Column(db.Integer, nullable=True)
    CapYear = db.Column(db.Integer, nullable=True)
    Remarks = db.Column(db.Text, nullable=True)
    Planned = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<MessierObject {self.Messier}>'
    
    def to_dict(self):
        return {field: getattr(self, field) for field in self.__table__.columns.keys()}
