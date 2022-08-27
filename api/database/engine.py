import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_HOST'),
    os.getenv('POSTGRES_PORT'),
    os.getenv('POSTGRES_DB'),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
DatabaseSession = sessionmaker(autocommit=False, bind=engine)
BaseModel = declarative_base()


def get_session() -> None:
    """
    Return session to database.

    Yields:
        Session
    """
    session = DatabaseSession()

    try:
        yield session
    except Exception:
        session.close()
