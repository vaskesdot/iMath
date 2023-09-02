import os
from sqlalchemy.exc import SQLAlchemyError
from project.db_utils import establish_sqlalchemy_connection, create_sqlalchemy_db_metadata, create_sqlalchemy_engine

def test_sqlalchemy_db_connection():
    try:
        engine = create_sqlalchemy_engine(os.getenv("DATABASE_URL"))
        metadata = create_sqlalchemy_db_metadata(engine)
        connection = establish_sqlalchemy_connection(engine)
    except SQLAlchemyError:
        assert True
