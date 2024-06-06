from flask import Flask

app = Flask(__name__)

from . import validador  # Importa as rotas do módulo validador
