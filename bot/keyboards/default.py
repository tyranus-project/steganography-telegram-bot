from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Encrypt"), KeyboardButton(text="Decrypt")]
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
