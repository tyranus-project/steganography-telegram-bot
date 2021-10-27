from aiogram import types
from aiogram.dispatcher import FSMContext

import os
import shutil


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
