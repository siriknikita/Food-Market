from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ('mysql+mysqlconnector://root:MySQL_Root-Password123!@localhost:3306'
                                         '/market')
app.config['SECRET_KEY'] = '76c8f410af9ca4c00cd1a89b'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
from market import routes