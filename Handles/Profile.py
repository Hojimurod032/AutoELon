from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DB.Request import get_user

profile_router = Router()
@profile_router.message(F.text =="👤 Mening hisobim")
async def profile(m: Message , state: FSMContext):
    tg_id = m.from_user.id
    user = get_user(tg_id)
    if not user:
        await m.answer("❌ Siz hali ro'yxatdan o'tmagansiz!")
        return
    text = f"""
    ----------------------------------
    👤 Profilingiz:

    🆔 ID: {user.tg_id}
    👨 Ism: {user.name}
    🎂 Yosh: {user.age}
    📞 Raqamingiz: {user.number}

    ----------------------------------
    """
    await m.answer(text)
