from flask import Flask
# from webapp import db, create_app
from webapp.__init__ import create_app
from webapp.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app) 

    with app.app_context():
        db.create_all()
