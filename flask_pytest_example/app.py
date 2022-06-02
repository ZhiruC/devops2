from flask import Flask
from flask_wtf.csrf import CSRFProtect
from handlers.routes import configure_routes

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

configure_routes(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
