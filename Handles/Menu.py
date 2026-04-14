from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from State.State import Register

menuRouter = Router()

@menuRouter.message(CommandStart())
async def start_command(m: Message, state: FSMContext):
    await m.answer(f"Assalomu alaykum hush kelibsiz: {m.from_user.full_name}")

    await m.answer("Ismingizni kiriting: ")
    await state.set_state(Register.name)


@menuRouter.message(Register.name)
async def state_name(m: Message, state: FSMContext):
    name = m.text
    await state.update_data(name=name)
    await m.answer("Yoshingizni kriting: ")
    await state.set_state(Register.age)


@menuRouter.message(Register.age)
async def state_age(m: Message, state: FSMContext):
    age = m.text
    await state.update_data(age=age)
    await m.answer("Telefon raqamingiz(+998")
    await state.set_state(Register.contact)


@menuRouter.message(Register.contact)
async def state_contact(m: Message, state: FSMContext):
    contact = m.text
    await state.update_data(contact=contact)
    await m.answer("Sizning malumotlaringniz saqlandi !")
