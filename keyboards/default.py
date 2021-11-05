from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Encrypt"), KeyboardButton(text="Decrypt")],
        [KeyboardButton(text="Settings"), KeyboardButton(text="Support")]
    ],
    resize_keyboard=True
)


encryption_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Start encryption again"), KeyboardButton(text="Cancel")]
    ],
    resize_keyboard=True
)


decryption_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Start decryption again"), KeyboardButton(text="Cancel")]
    ],
    resize_keyboard=True
)
