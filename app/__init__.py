from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
<<<<<<< HEAD
from flask_mail import Mail
from os import *
=======
# from flask_migrate import Migrate
from flask_mail import Mail
# from flask_uploads import UploadSet,configure_uploads,IMAGES
>>>>>>> 2583607409e4dc74893d4796afb42b43198177a2


mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()



def create_app(config_name):

    app = Flask(__name__)
    
    # Initializing configurations
    app.config.from_object(config_options[config_name])

    # Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    


    return app 

