from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import FileIsTooBig

from app import config
from app.keyboards.default import main_menu_keyboard, decryption_keyboard
from app.utils.misc import decrypt_stego_image
from app.utils.misc import reset_user_data
from app.utils.misc import save_user_image
from app.utils.states import Decrypt


async def start_decrypt(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Send an image with a hidden and encrypted message in it",
        reply_markup=decryption_keyboard
    )
    await message.answer(
        "IMPORTANT!\n"
        "The image must be sent as a file"
    )
    await Decrypt.waiting_for_stego_image.set()


async def enter_stego_image(message: types.Message, state: FSMContext):
    if message.content_type == "photo":
        await message.answer("The image must be sent as a file. Try again!")
        return
    elif message.document.mime_type.split('/')[0] != "image":
        await message.answer("The file you sent is not an image. Try again!")
        return
    else:
        try:
            user_file_as_image = await save_user_image(message, "png")
        except FileIsTooBig:
            await message.reply(
                "Your image is too big!\n"
                "It is unlikely that there was something hidden in it with the help of this bot...\n"
                "You can try again!"
            )
        else:
            await message.answer("Enter the password to find out the message hidden in the sent image")
            await state.update_data(stego_image=user_file_as_image)
            await Decrypt.next()


async def enter_decryption_key(message: types.Message, state: FSMContext):
    await state.update_data(decryption_key=message.text)
    user_data = await state.get_data()
    try:
        decrypted_message_text = decrypt_stego_image(**user_data, bot_salt=config.BOT_SALT)
    except Exception:
        await message.answer(
            "Something went wrong. Start again!",
            reply_markup=main_menu_keyboard
        )
    else:
        if decrypted_message_text:
            await message.answer("The secret message that contained the image is posted below")
            await message.answer(
                f"{decrypted_message_text}",
                reply_markup=main_menu_keyboard
            )
        else:
            await message.answer(
                "Nothing is encrypted in the image, or your password is incorrect",
                reply_markup=main_menu_keyboard
            )
    finally:
        await reset_user_data(message, state)


def register_decryption_handlers(dp: Dispatcher):
    dp.register_message_handler(start_decrypt, Text(equals="Decrypt", ignore_case=True))
    dp.register_message_handler(start_decrypt, Text(equals="Start decryption again"), state="*")
    dp.register_message_handler(enter_stego_image, content_types=["document", "photo"], state=Decrypt.waiting_for_stego_image)
    dp.register_message_handler(enter_decryption_key, state=Decrypt.waiting_for_decryption_key)
