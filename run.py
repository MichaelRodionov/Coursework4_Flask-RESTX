from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from app.views.favorites import fav_ns
from config import Config
from setup_db import db
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns

api = Api()


# ----------------------------------------------------------------
# create app, register extensions, create tables
def create_app(config_object: Config):
    """
    This function is called to create Flask application
    :param config_object: Config
    :return: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    """
    This function is called to register extensions init database and create api
    :param app: Flask application
    """
    db.init_app(app)
    CORS(app)
    api.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(fav_ns)
    create_data(app, db)


def create_data(app, database):
    """Creating table"""
    with app.app_context():
        database.create_all()


application = create_app(Config())


if __name__ == '__main__':
    application.run(port=5000)
