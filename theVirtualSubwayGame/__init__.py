from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from theVirtualSubwayGame.flaskSecretKey import get_api_key

app = Flask(__name__)
app.config['SECRET_KEY'] = get_flask_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stations.db'
db = SQLAlchemy(app)

from theVirtualSubwayGame import routes
