from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///validators.db'
db = SQLAlchemy(app)

from . import seletor  # Importa as rotas do módulo seletor
