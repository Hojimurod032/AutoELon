from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from Data.config import DB_URL

engine = create_engine(DB_URL)


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)
