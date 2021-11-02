import os
import shutil

from aiogram import types
from aiogram.dispatcher import FSMContext

from cryptosteganography import CryptoSteganography

from config import BOT_SALT


async def save_user_file_as_image(message: types.Message, raster_format: str):
    image_save_path = f"data/{message.from_user.id}/{message.document.file_id}.{raster_format}"
    await message.document.download(destination_file=image_save_path)
    return image_save_path


async def reset_user_data(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.reset_state()
    if os.path.isdir(f"data/{message.from_user.id}"):
        shutil.rmtree(f"data/{message.from_user.id}")


def create_encrypted_stego_image(secret_message, image_container, encryption_key):
    crypto_steganography = CryptoSteganography(encryption_key)
    encrypted_stego_container_path = f"{image_container.split('_', 1)[0]}_image.png"
    crypto_steganography.hide(image_container, encrypted_stego_container_path, secret_message)
    return encrypted_stego_container_path


async def decrypting_function(image_to_decrypt, password_to_decrypt, salt=BOT_SALT):
    crypto_steganography = CryptoSteganography(password_to_decrypt + salt)
    secret_text = crypto_steganography.retrieve(image_to_decrypt)
    if secret_text is None:
        crypto_steganography = CryptoSteganography(password_to_decrypt)
        secret_text = crypto_steganography.retrieve(image_to_decrypt)
    return secret_text
