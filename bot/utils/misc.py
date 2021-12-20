import hashlib
import os
import shutil
import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext

from cryptosteganography import CryptoSteganography

from bot.config import DATA_DIR, SESSION_SALT


def hash_id(user_id: int, use_salt: bool = True) -> str:
    hashing_id = str(user_id).encode()
    hashed_id = hashlib.sha256(hashing_id + SESSION_SALT.encode()) if use_salt else hashlib.sha256(hashing_id)
    return hashed_id.hexdigest()


async def reset_user_data(message: types.Message, state: FSMContext = None) -> None:
    if state and await state.get_state():
        await state.reset_state()
    if os.path.isdir(f"{DATA_DIR}/{hash_id(message.from_user.id)}"):
        shutil.rmtree(f"{DATA_DIR}/{hash_id(message.from_user.id)}")


async def save_user_image(message: types.Message, raster_format: str = "jpg") -> str:
    image_save_path = f"{DATA_DIR}/{hash_id(message.from_user.id)}/{uuid.uuid4()}.{raster_format}"
    if message.content_type == "document":
        await message.document.download(destination_file=image_save_path)
    else:
        await message.photo[-1].download(destination_file=image_save_path)
    return image_save_path


def create_encrypted_stego_image(secret_message: str, image_container: str, encryption_key: str) -> str:
    crypto_steganography = CryptoSteganography(encryption_key)
    encrypted_stego_container_path = f"{os.path.dirname(image_container)}/{str(uuid.uuid4()).split('-')[-1]}.png"
    crypto_steganography.hide(image_container, encrypted_stego_container_path, secret_message)
    return encrypted_stego_container_path


def decrypt_stego_image(stego_image: str, decryption_key: str) -> str:
    crypto_steganography = CryptoSteganography(decryption_key)
    secret_message = crypto_steganography.retrieve(stego_image)
    if secret_message is None:
        crypto_steganography = CryptoSteganography(decryption_key)
        secret_message = crypto_steganography.retrieve(stego_image)
    return secret_message
