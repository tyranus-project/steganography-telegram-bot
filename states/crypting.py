from aiogram.dispatcher.filters.state import StatesGroup, State


class Encrypting(StatesGroup):
    waiting_for_message = State()
    waiting_for_image = State()
    waiting_for_password = State()


class Decrypting(StatesGroup):
    waiting_for_image = State()
    waiting_for_password = State()
