"""
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from dependences import I18N_DOMAIN, LOCAL_DIR
from typing import Tuple, Any


async def get_lang(user_id):
    return None


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale


def setup_middleware(dp):
    i18n = ACLMiddleware(I18nMiddleware, LOCAL_DIR)
    dp.middleware.setup(i18n)
    return i18n
"""