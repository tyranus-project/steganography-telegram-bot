from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


async def decrypting_start(message: types.Message, state: FSMContext):
    pass


async def encrypted_image_entering(message: types.Message, state: FSMContext):
    pass


async def decryption_password_entering_decrypting_end(message: types.Message, state: FSMContext):
    pass


def register_handlers_decryption(dp: Dispatcher):
    pass
