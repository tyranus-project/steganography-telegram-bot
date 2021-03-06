from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.utils.keyboards import decryption_keyboard, main_menu_keyboard
from bot.utils.misc import LENGTH_LIMIT, decrypt_stego_image, reset_user_data, save_container_image
from bot.utils.states import Decryption


async def start_decryption_process(message: types.Message, state: FSMContext):
    """Resets the current user data and switches to the state of waiting for a stego image from the user."""
    await reset_user_data(message, state)
    await message.answer("Send your stego image – the image with a hidden and encrypted message in it.")
    await message.answer(
        "<b>Important!</b>\n"
        "The image must be sent as a file.",
        reply_markup=decryption_keyboard
    )
    await Decryption.stego_image.set()


async def add_stego_image(message: types.Message, state: FSMContext):
    """Gets and saves the stego image and switches to the state of waiting for a decryption key from the user."""
    if message.content_type == "photo":
        await message.reply("The image must be sent as a file. Try again.")
    elif message.document.mime_type.split('/')[0] != "image":
        await message.reply("The file you sent is not an image. Try again.")
    else:
        stego_image = await save_container_image(message)
        await state.update_data(stego_image=stego_image)
        await message.answer("Enter the password to find out the message hidden in the sent image.")
        await Decryption.next()


async def add_decryption_key(message: types.Message, state: FSMContext):
    """Ends the decryption process by sending the secret text message to the user and resets the current user data."""
    if len(message.text) == LENGTH_LIMIT:
        await message.reply("Please note that this message will be used as your password.")
    await state.update_data(decryption_key=message.text)
    user_data = await state.get_data()
    decrypted_message_text = decrypt_stego_image(**user_data)
    if decrypted_message_text:
        await message.answer("The secret message that contained the stego image is posted below.")
        await message.answer(
            f"{decrypted_message_text}",
            reply_markup=main_menu_keyboard
        )
    else:
        await message.answer(
            "Nothing is encrypted in the image, or your password is incorrect.",
            reply_markup=main_menu_keyboard
        )
    await reset_user_data(message, state)


def register_decryption_handlers(dp: Dispatcher):
    """Sets the decryption process handlers."""
    dp.register_message_handler(start_decryption_process, commands=["decrypt"], state="*")
    dp.register_message_handler(start_decryption_process, Text(equals="🔓 Decrypt", ignore_case=True))
    dp.register_message_handler(start_decryption_process, Text(equals="Start decryption again"), state=Decryption.states_names)
    dp.register_message_handler(add_stego_image, content_types=["document", "photo"], state=Decryption.stego_image)
    dp.register_message_handler(add_decryption_key, state=Decryption.decryption_key)
