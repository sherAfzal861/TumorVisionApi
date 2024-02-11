
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import db, ma
from marshmallow import fields


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    images = relationship('Image', backref='user', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    prediction_results = db.Column(db.Text)
    confidence = db.Column(db.Float)
    prediction_date = db.Column(db.DateTime)
    reports = relationship('Report', backref='image', lazy=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    report_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    report_text = db.Column(db.Text, nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True

class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image
        load_instance = True

class ReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Report
        load_instance = True

    user_id = fields.Integer()
    image_id = fields.Integer()

user_schema = UserSchema()
image_schema = ImageSchema()
report_schema = ReportSchema()