from aiogram import Dispatcher

from loguru import logger

from app.config import THROTTLING_RATE_LIMIT

from .throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher):
    logger.info("Configure middlewares...")
    dp.setup_middleware(ThrottlingMiddleware(THROTTLING_RATE_LIMIT))
