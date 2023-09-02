import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger

from project.db_utils import create_sqlalchemy_engine, create_sqlalchemy_db_metadata, establish_sqlalchemy_connection

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MAX_CONTENT_LENGTH = 1024
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_REMOTE")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"


engine_sqlite = create_sqlalchemy_engine('sqlite:///project/data.db')
metadata_sqlite = create_sqlalchemy_db_metadata(engine_sqlite)
connection_sqlite = establish_sqlalchemy_connection(engine_sqlite)

engine_psql = create_sqlalchemy_engine(Config.SQLALCHEMY_DATABASE_URI)
metadata_psql = create_sqlalchemy_db_metadata(engine_psql)
connection_psql = establish_sqlalchemy_connection(engine_psql)
session_psql = sessionmaker(bind=engine_psql)

logging = logger.add("logging.json", format='{time} {level} {message}', serialize=True, retention=3,
           rotation="100 MB")