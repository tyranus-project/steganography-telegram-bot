from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


encryption_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Start encryption again"),
            KeyboardButton(text="Cancel")
        ]
    ],
    resize_keyboard=True
)

decryption_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Start decryption again"),
            KeyboardButton(text="Cancel")
        ]
    ],
    resize_keyboard=True
)
