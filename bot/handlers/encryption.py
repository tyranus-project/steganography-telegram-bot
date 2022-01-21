from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.utils.keyboards import encryption_keyboard, main_menu_keyboard
from bot.utils.misc import LENGTH_LIMIT, encrypt_stego_image, reset_user_data, save_container_image
from bot.utils.states import Encryption


async def start_encryption_process(message: types.Message, state: FSMContext):
    """Resets the current user data and switches to the state of waiting for a cover image from the user."""
    await reset_user_data(message, state)
    await message.answer(
        "Send your cover image - the image in which your secret message will be hidden and encrypted.",
        reply_markup=encryption_keyboard
    )
    await Encryption.cover_image.set()


async def add_cover_image(message: types.Message, state: FSMContext):
    """Gets and saves the cover image and switches to the state of waiting for a secret text message from the user."""
    if message.content_type == "document" and message.document.mime_type.split('/')[0] != "image":
        await message.reply("The file you sent is not an image. Try again.")
        return
    cover_image = await save_container_image(message)
    await state.update_data(cover_image=cover_image)
    await message.answer("Enter the secret text message you want to encrypt.")
    await Encryption.next()


async def add_secret_message(message: types.Message, state: FSMContext):
    """Receives the secret text message and switches to the state of waiting for an encryption key from the user."""
    if len(message.text) == LENGTH_LIMIT:
        await message.reply("Please note that this message will be encrypted.")
    await state.update_data(secret_message=message.text)
    await message.answer("Enter the password to encrypt now and decrypt later.")
    await Encryption.next()


async def add_encryption_key(message: types.Message, state: FSMContext):
    """Ends the encryption process by sending the encrypted stego image to the user and resets the current user data."""
    if len(message.text) == LENGTH_LIMIT:
        await message.reply("Please note that this message will be used as your password.")
    await state.update_data(encryption_key=message.text)
    user_data = await state.get_data()
    stego_image = encrypt_stego_image(**user_data)
    await message.answer_document(types.InputFile(stego_image))
    await message.answer(
        "Stego image successfully created. Your secret text message is hidden and encrypted in the image above.",
        reply_markup=main_menu_keyboard
    )
    await reset_user_data(message, state)


def register_encryption_handlers(dp: Dispatcher):
    """Sets the encryption process handlers."""
    dp.register_message_handler(start_encryption_process, commands=["encrypt"], state="*")
    dp.register_message_handler(start_encryption_process, Text(equals="🔐 Encrypt", ignore_case=True))
    dp.register_message_handler(start_encryption_process, Text(equals="Start encryption again"), state=Encryption.states_names)
    dp.register_message_handler(add_secret_message, state=Encryption.secret_message)
    dp.register_message_handler(add_cover_image, content_types=["document", "photo"], state=Encryption.cover_image)
    dp.register_message_handler(add_encryption_key, state=Encryption.encryption_key)
