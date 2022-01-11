from aiogram.dispatcher.filters.state import State, StatesGroup


class Encryption(StatesGroup):
    cover_image = State()
    secret_message = State()
    encryption_key = State()


class Decryption(StatesGroup):
    stego_image = State()
    decryption_key = State()


cryption_states = Encryption.states_names + Decryption.states_names
