from aiogram.dispatcher.filters.state import StatesGroup, State


class Encrypt(StatesGroup):
    waiting_for_secret_message = State()
    waiting_for_image_container = State()
    waiting_for_encryption_key = State()


class Decrypt(StatesGroup):
    waiting_for_stego_image = State()
    waiting_for_decryption_key = State()
