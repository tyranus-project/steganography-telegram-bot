import os
import shutil

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import FileIsTooBig

from cryptosteganography import CryptoSteganography


async def save_user_file_as_image(message: types.Message, raster_format: str):
    try:
        image_save_path = f"app/data/{message.from_user.id}/{message.message_id}.{raster_format}"
        if message.content_type == "document":
            await message.document.download(destination_file=image_save_path)
        else:
            await message.photo[-1].download(destination_file=image_save_path)
    except FileIsTooBig:
        raise
    else:
        return image_save_path


async def reset_user_data(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.reset_state()
    if os.path.isdir(f"app/data/{message.from_user.id}"):
        shutil.rmtree(f"app/data/{message.from_user.id}")


def create_encrypted_stego_image(secret_message, image_container, encryption_key):
    crypto_steganography = CryptoSteganography(encryption_key)
    encrypted_stego_container_path = f"{image_container.split('.')[0]}.png"
    crypto_steganography.hide(image_container, encrypted_stego_container_path, secret_message)
    return encrypted_stego_container_path


def decrypt_stego_image(stego_image, decryption_key, bot_salt):
    crypto_steganography = CryptoSteganography(decryption_key + bot_salt)
    secret_message = crypto_steganography.retrieve(stego_image)
    if secret_message is None:
        crypto_steganography = CryptoSteganography(decryption_key)
        secret_message = crypto_steganography.retrieve(stego_image)
    return secret_message
