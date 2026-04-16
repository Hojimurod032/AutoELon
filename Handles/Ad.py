from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from DB.Request import save_cars
from Keyboard.Reply import main_menu
from State.State import Car

ad_router = Router()
@ad_router.message(F.text == "📢 E’lon joylash")
async def add_cars(m: Message, state: FSMContext):
    await m.answer("🚗 Moshinani nomini kiriting: ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Car.title)

@ad_router.message(Car.title)
async def state_title(m: Message, state: FSMContext):
    await state.update_data(title=m.text)
    await m.answer("📅 Moshinani yilini kiriting: ")
    await state.set_state(Car.age)

@ad_router.message(Car.age)
async def state_age(m: Message, state: FSMContext):
    await state.update_data(age=m.text)
    await m.answer("💰 Moshinani narxini kiriting: ")
    await state.set_state(Car.price)


@ad_router.message(Car.price)
async def state_price(m: Message, state: FSMContext):
    await state.update_data(price=m.text)
    await m.answer("📞 Bog'lanish uchun telefon raqamni kiriting: ")
    await state.set_state(Car.user_number)


@ad_router.message(Car.user_number)
async def state_number(m: Message, state: FSMContext):
    await state.update_data(user_number=m.text)
    data = await state.get_data()
    title = data.get('title')
    age = data.get('age')
    price = data.get('price')
    user_number = data.get('user_number')
    user_id = m.from_user.id
    save_cars(title=title, age=age, price=price, user_number=user_number, user_id=user_id)
    markup = main_menu()
    await m.answer("✅ Sizning e'loningiz joylandi!", reply_markup=markup)
    await state.clear()