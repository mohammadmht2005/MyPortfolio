from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = "ec29e9c6c1116fe18003de25ffa6805200e8711d42ab0cadce7e85b52d07b8c7"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mail = Mail(app)

from portfolio import routes