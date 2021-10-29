from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


support_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="FAQ", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Instructions", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Author's channel", url="https://telegram.org/faq")],
        [InlineKeyboardButton(text="Support the author", callback_data="support the author")],
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
