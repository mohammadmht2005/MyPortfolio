from flask import render_template,url_for,flash,redirect,request,abort
from portfolio import app,mail
from flask_mail import Message
from portfolio.forms import *
from werkzeug.exceptions import NotFound

@app.route("/")
@app.route("/index",methods=["GET"])
def home():
    return render_template("index.html")

