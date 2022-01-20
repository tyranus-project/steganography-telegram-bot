from aiogram import Dispatcher

from loguru import logger

from .throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher):
    """Sets all bot middlewares."""
    logger.info("Configure middlewares...")
    dp.setup_middleware(ThrottlingMiddleware(limit=0.5))
