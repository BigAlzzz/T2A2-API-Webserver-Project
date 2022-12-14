from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.shoes_controller import shoes_bp
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
import os
from init import db , ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):
        return {'error':str(err)}, 404
    
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error':str(err)}, 401

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(shoes_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)


    return app