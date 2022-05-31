import logging
from aiogram.utils import executor
from dependences import dp
from handlers import commands
from DataBase.db_managing import db_connect
from user import admin_set


# Configure logging
logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Bot is online')


def main():
    db_connect()
    admin_set.list_handlers_admin(dp)
    commands.list_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
