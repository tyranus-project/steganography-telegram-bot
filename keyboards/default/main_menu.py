from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Encrypt"), KeyboardButton(text="Decrypt")],
        [KeyboardButton(text="Settings"), KeyboardButton(text="Support")]
    ],
    resize_keyboard=True
)
