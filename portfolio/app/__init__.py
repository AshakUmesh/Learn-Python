from flask import Flask
from .config import Config
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Optional: Only use db if flask_sqlalchemy is installed
    try:
        from .extensions import db
        db.init_app(app)
    except ImportError:
        pass  # Database not needed for this portfolio site

    Talisman(app)

    from .main.routes import main
    app.register_blueprint(main)

    return app
