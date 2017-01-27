from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_CONN_STRING")
db = SQLAlchemy(app)

class Compliment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))

    def __init__(self, compliment):
        self.text = compliment

    def __repr__(self):
        return '<Compliment %r>' % self.text
