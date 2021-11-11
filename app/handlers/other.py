from aiogram import types, Dispatcher
from aiogram.types.message import ContentType


async def undefined_request(message: types.Message):
    await message.answer(
        "Use the menu buttons and commands, and follow the instructions in the messages\n\n"
        "/help to show user manual\n"
        "/start to restart the bot"
    )


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(undefined_request, content_types=ContentType.ANY, state="*")
