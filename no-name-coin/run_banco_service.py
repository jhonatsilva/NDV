from flask import Flask
from banco_service.routes import banco_bp

app = Flask(__name__)
app.register_blueprint(banco_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(port=6000)
