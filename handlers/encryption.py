from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


async def encrypting_start(message: types.Message, state: FSMContext):
    pass


async def secret_message_entering(message: types.Message, state: FSMContext):
    pass


async def original_image_entering(message: types.Message, state: FSMContext):
    pass


async def encryption_password_entering_encrypting_end(message: types.Message, state: FSMContext):
    pass


def register_handlers_encryption(dp: Dispatcher):
    pass
