from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.keyboards.default import main_menu_keyboard, encryption_keyboard
from bot.utils.misc import create_encrypted_stego_image, reset_user_data, save_user_image
from bot.utils.states import Encrypt


async def start_encrypt(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Enter the secret text you want to encrypt",
        reply_markup=encryption_keyboard
    )
    await Encrypt.waiting_for_secret_message.set()


async def enter_secret_message(message: types.Message, state: FSMContext):
    if len(message.text) == 4096:
        await message.reply("Please note that this message will be encrypted")
    await state.update_data(secret_message=message.text)
    await message.answer("Send the image in which the secret text will be hidden and encrypted")
    await Encrypt.next()


async def enter_image_container(message: types.Message, state: FSMContext):
    if message.content_type == "document" and message.document.mime_type.split('/')[0] != "image":
        await message.reply("The file you sent is not an image. Try again!")
        return
    user_image = await save_user_image(message)
    await message.answer("Enter the password to encrypt your secret text now and decrypt later")
    await state.update_data(image_container=user_image)
    await Encrypt.next()


async def enter_encryption_key(message: types.Message, state: FSMContext):
    if len(message.text) == 4096:
        await message.reply("Please note that this message will be used as your password")
    await state.update_data(encryption_key=message.text)
    user_data = await state.get_data()
    encrypted_stego_container = create_encrypted_stego_image(**user_data)
    await message.answer_document(types.InputFile(encrypted_stego_container))
    await message.answer(
        "Your text is hidden and encrypted in the file above",
        reply_markup=main_menu_keyboard
    )
    await reset_user_data(message, state)


def register_encryption_handlers(dp: Dispatcher):
    dp.register_message_handler(start_encrypt, Text(equals="Encrypt", ignore_case=True))
    dp.register_message_handler(start_encrypt, Text(equals="Start encryption again"), state=Encrypt.states_names)
    dp.register_message_handler(enter_secret_message, state=Encrypt.waiting_for_secret_message)
    dp.register_message_handler(enter_image_container, content_types=["document", "photo"], state=Encrypt.waiting_for_image_container)
    dp.register_message_handler(enter_encryption_key, state=Encrypt.waiting_for_encryption_key)