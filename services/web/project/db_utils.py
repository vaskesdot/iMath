from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, MetaData



def create_sqlalchemy_engine(url: str):
    try:
        engine = create_engine(url)
        return engine
    except:
        raise SQLAlchemyError('The Error has occurred while creating engine')


def create_sqlalchemy_db_metadata(sqlalchemy_engine):
    try:
        metadata = MetaData()
        metadata.reflect(bind=sqlalchemy_engine)
        return metadata
    except:
        raise SQLAlchemyError('The Error has occurred while creating metadata')


def establish_sqlalchemy_connection(sqlalchemy_engine):
    try:
        connection = sqlalchemy_engine.connect()
        return connection
    except:
        raise SQLAlchemyError('The Error has occurred while establishing sqlalchemy connection')


