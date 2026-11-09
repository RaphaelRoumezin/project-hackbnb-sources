from os import path

basedir = path.abspath(path.dirname(__file__))

CORS_ORIGINS = []

SQLALCHEMY_DATABASE_URI = "sqlite:///./database.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False
