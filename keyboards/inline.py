from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def call_settings_keyboard(bot_salt_status):
    ability = "No" if bot_salt_status else "Yes"
    settings_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
                [InlineKeyboardButton(f"Ability to decrypt with other tools: {ability}", callback_data="change")],
                [InlineKeyboardButton("Hide", callback_data="hide")]
        ]
    )
    return settings_keyboard


support_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="FAQ", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Instructions", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Author's channel", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Support the author", callback_data="donate")],
        [InlineKeyboardButton(text="Hide", callback_data="hide")]
    ]
)


donate_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bitcoin (BTC)", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Monero (XMR)", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Back", callback_data="back")],
        [InlineKeyboardButton(text="Hide", callback_data="hide")]
    ]
)
