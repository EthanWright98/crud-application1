from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid


app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes