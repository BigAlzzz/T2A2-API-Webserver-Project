from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from init import db , ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.route('/')
    def index():
        return 'Hello'

    return app