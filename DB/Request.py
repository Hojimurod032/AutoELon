from sqlalchemy import select
from sqlalchemy.orm import Session

from DB.SQLARCHERY import engine, User, Cars

def get_user(tg_id):
    with Session(engine) as session:
        user = session.execute(select(User).where(User.tg_id == tg_id)).scalar()
        return user

def save_user(tg_id, name, age, number):
    with Session(engine) as session:
        user = session.execute(select(User).where(User.tg_id == tg_id)).scalar()
        if not user:
            new_use = User(tg_id=tg_id, name=name, age=age, number=number)
            session.add(new_use)
            session.commit()


def save_cars(title, age, price, user_number, user_id):
    with Session(engine) as session:
        new_car = Cars(title=title, age=age, price=price, user_number=user_number, user_id=user_id)
        session.add(new_car)
        session.commit()
