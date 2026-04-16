from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from DB.Request import save_user, get_user
from Keyboard.Reply import main_menu
from State.State import Register

menuRouter = Router()
@menuRouter.message(CommandStart())
async def start_command(m: Message, state: FSMContext):
    await m.answer(f"Assalomu alaykum hush kelibsiz: {m.from_user.full_name}")
    tg_id = m.from_user.id
    markup = main_menu()
    data = get_user(tg_id)
    if data:
        await m.answer("Siz oldin royxatdan otgansz", reply_markup=markup)
    else:
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
    tg_id = m.from_user.id
    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    markup = main_menu()
    save_user(tg_id=tg_id, name=name, age=age, number=contact)
    await m.answer("Sizning malumotlaringniz saqlandi !", reply_markup=markup)
    await state.clear()
