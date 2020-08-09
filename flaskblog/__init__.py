from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from elasticsearch import Elasticsearch
from flask import request
from flask_babel import Babel , gettext , lazy_gettext as _l

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['ELASTICSEARCH_URL']='http://localhost:9200'
app.config['LANGUAGES']=['en']
app.config['POSTS_PER_PAGE']=3
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
babel = Babel(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    if app.config['ELASTICSEARCH_URL'] else None


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


from flaskblog import routes
from flaskblog import test