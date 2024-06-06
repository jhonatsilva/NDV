from flask import Flask
from validador_service.routes import validador_bp

app = Flask(__name__)
app.register_blueprint(validador_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(port=6002)
