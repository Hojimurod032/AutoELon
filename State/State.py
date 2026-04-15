from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    name = State()
    age = State()
    contact = State()


class Car(StatesGroup):
    title = State()
    age = State()
    price = State()
    user_number = State()
