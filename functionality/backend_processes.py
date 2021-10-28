from aiogram import types
from aiogram.dispatcher import FSMContext

import os
import shutil

from cryptosteganography import CryptoSteganography


async def download_document_as_image(message: types.Message, raster_format: str):
    os.mkdir(f"data/{message.from_user.id}")
    document_as_image_save_path = f"data/{message.from_user.id}/{message.document.file_id}.{raster_format}"
    await message.document.download(document_as_image_save_path, make_dirs=True)
    return document_as_image_save_path


async def reset_state_delete_user_data(message: types.Message, state: FSMContext):
    """
    print("Calling", reset_state_delete_user_data)
    current_state = await state.get_state()
    if current_state:
        print("Last state:", current_state)
    """
    await state.reset_state()
    if os.path.isdir(f"data/{message.from_user.id}"):
        shutil.rmtree(f"data/{message.from_user.id}")


async def encrypting_function(message_to_encrypt, image_to_encrypt, password_to_encrypt):
    crypto_steganography = CryptoSteganography(password_to_encrypt)
    crypto_steganography.hide(image_to_encrypt, f"{image_to_encrypt.split('_', 1)[0]}_image.png", message_to_encrypt)
    return f"{image_to_encrypt.split('_', 1)[0]}_image.png"


async def decrypting_function(image_to_decrypt, password_to_decrypt):
    crypto_steganography = CryptoSteganography(password_to_decrypt)
    secret_text = crypto_steganography.retrieve(image_to_decrypt)
    return secret_text