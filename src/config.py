from flask_mail import Mail, Message
from flask_cors import CORS
from flask import Flask, request, jsonify 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pathlib

basedir = pathlib.Path(__file__).parent.resolve()
app = Flask(__name__)
CORS(app, origins='http://localhost:63296')
app.secret_key = 'eb4daff29821d12d5e0a9bb85566c42b'
app.config['JWT_SECRET_KEY'] = '09b439697e4c390480d8e81443d261bdf0368b9751f447b1abba7f7c347a7331'
jwt = JWTManager(app)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'sherafzalg666@gmail.com'
app.config['MAIL_PASSWORD'] = 'wdqz fxxw vmma uxis'

mail = Mail(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'tumorvision.db'}"
print(f"sqlite:///{basedir / 'tumorvision.db'}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)