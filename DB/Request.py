from sqlalchemy.orm import Session

from DB.SQLARCHERY import engine


def save_user():
    with Session(engine) as session:
        pass
