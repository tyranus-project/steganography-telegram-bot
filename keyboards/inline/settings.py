from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def call_settings_keyboard(bot_salt_status):
    ability = "No" if bot_salt_status else "Yes"
    settings_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
                [InlineKeyboardButton(text=f"Ability to decrypt with other tools: {ability}", callback_data="change")],
                [InlineKeyboardButton(text="Hide", callback_data="hide")]
        ]
    )
    return settings_keyboard
