import os
from flask import Flask

from .config import Config, DATA_DIR
from .extensions import db, migrate
from .routes import api



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(DATA_DIR, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)

    #Note the url_prefix -> all the routes associated with this blueprint will start with /exercises
    app.register_blueprint(api, url_prefix="/exercises")

    return app