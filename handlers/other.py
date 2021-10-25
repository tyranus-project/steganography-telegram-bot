from aiogram import types, Dispatcher
from aiogram.types.message import ContentType


async def undefined_request(message: types.Message):
    channel_name = "@channel_name"
    undefined_message = ("For Bot requests use...",
                         f"{channel_name}")
    await message.answer("\n\n".join(undefined_message))


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(undefined_request, content_types=ContentType.ANY, state="*")
