from aiogram import types

import os


async def download_document_as_image(message: types.Message, raster_format: str):
    os.mkdir(f"data/{message.from_user.id}")
    document_as_image_save_path = f"data/{message.from_user.id}/{message.document.file_id}.{raster_format}"
    await message.document.download(document_as_image_save_path, make_dirs=True)
    return document_as_image_save_path
