from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_caching import Cache
from flask_whooshee import Whooshee


db = SQLAlchemy()



bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
cache = Cache()
whooshee = Whooshee()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    # with app.app_context():
    #     # Extensions like Flask-SQLAlchemy now know what the "current" app
    #     # is while within this block. Therefore, you can now run........
    #     #https://stackoverflow.com/questions/19437883/when-scattering-flask-models-runtimeerror-application-not-registered-on-db-w
    #     db.create_all()

    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
  
    
    return app
