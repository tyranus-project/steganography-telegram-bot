from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher):
    dp.setup_middleware(ThrottlingMiddleware(.5))
