from os import path


# ----------------------------------------------------------------
# configuration class
class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.abspath(path.join("data", "movies.db"))}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_PRETTYPRINT_REGULAR = True
    JSON_AS_ASCII = False
    DEBUG = True
