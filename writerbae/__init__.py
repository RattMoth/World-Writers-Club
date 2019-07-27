from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ifgdfnaocvytvk:84c1e3a50005ae17de34b009a3d4c15992f035843cc2fea7682d5a5436898690@ec2-54-243-193-59.compute-1.amazonaws.com:5432/ddnq3pibrcqgp8"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #blueprint for routes that require auth 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


""" 
so the objects of this app
User
Prompt Session
Writing

User + User meet in a Prompt Session and create Writings which are sent to each other
"""


