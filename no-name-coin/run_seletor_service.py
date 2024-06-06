from flask import Flask
from seletor_service.routes import seletor_bp

app = Flask(__name__)
app.register_blueprint(seletor_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(port=6001)
