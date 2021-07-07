from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy.sql import exists

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webdatabase.db'
app.config['SECRET_KEY'] = 'e11fe5e32f76d6bdc6adec7b'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)#generate has hashpasswords
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category="info"

from webfiles import routes