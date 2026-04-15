from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🚗 Mashina sotib olish")],
            [KeyboardButton(text="📢 E’lon joylash")],
            [KeyboardButton(text="👤 Mening hisobim")]
        ],
        resize_keyboard=True
    )
