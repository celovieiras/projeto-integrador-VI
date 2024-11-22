from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = ""

db = SQLAlchemy(app)

from projeto_integrador_vi import routes