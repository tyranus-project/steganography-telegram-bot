import hashlib
import os
import shutil
import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext

from cryptosteganography import CryptoSteganography

from bot.config import DATA_DIR, SESSION_SALT


# Telegram has a limit when sending message of 4096 chars
LENGTH_LIMIT = 4096


def hash_user_id(user_id: int, use_salt: bool = True) -> str:
    """Hashes the passed identifier using SHA-256 and optionally adding the session salt."""
    hashing_id = str(user_id).encode()
    hashed_id = hashlib.sha256(hashing_id + SESSION_SALT.encode()) if use_salt else hashlib.sha256(hashing_id)
    return hashed_id.hexdigest()


async def reset_user_data(message: types.Message, state: FSMContext = None) -> None:
    """Resets the current user state and user data (if passed and present)."""
    if state and await state.get_state():
        await state.reset_state()
    if os.path.isdir(f"{DATA_DIR}/{hash_user_id(message.from_user.id)}"):
        shutil.rmtree(f"{DATA_DIR}/{hash_user_id(message.from_user.id)}")


async def save_container_image(message: types.Message, raster_format: str = "jpg") -> str:
    """Downloads and saves a file from the user message as an image in the desired format and hashes its name."""
    container_image_save_path = f"{DATA_DIR}/{hash_user_id(message.from_user.id)}/{uuid.uuid4()}.{raster_format}"
    if message.content_type == "document":
        await message.document.download(destination_file=container_image_save_path)
    else:
        await message.photo[-1].download(destination_file=container_image_save_path)
    return container_image_save_path


def encrypt_stego_image(cover_image: str, secret_message: str, encryption_key: str) -> str:
    """Encrypts using AES-256 and saves the data inside the image."""
    crypto_steganography = CryptoSteganography(encryption_key)
    stego_image_path = f"{os.path.dirname(cover_image)}/{str(uuid.uuid4()).split('-')[-1]}.png"
    crypto_steganography.hide(cover_image, stego_image_path, secret_message)
    return stego_image_path


def decrypt_stego_image(stego_image: str, decryption_key: str) -> str:
    """Retrieves the encrypted data from the image."""
    crypto_steganography = CryptoSteganography(decryption_key)
    secret_message = crypto_steganography.retrieve(stego_image)
    return secret_message
