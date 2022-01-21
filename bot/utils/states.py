from aiogram.dispatcher.filters.state import State, StatesGroup


class Encryption(StatesGroup):
    """Class for the encryption process states."""
    cover_image = State()
    secret_message = State()
    encryption_key = State()


class Decryption(StatesGroup):
    """Class for the decryption process states."""
    stego_image = State()
    decryption_key = State()


cryption_states_names = Encryption.states_names + Decryption.states_names
