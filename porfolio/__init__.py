from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-fallback-key')  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mail = Mail(app)

from portfolio import routes
