from aiogram import types
from dependences import admin_id
from DataBase.db_managing import count_users, name_users


# Checking if user is an admin of a bot
async def check_admin(message: types.Message):

    if message.from_user.id == admin_id:
        await message.answer("To get statistic click /admin_rights")
    else:
        await message.answer("You're not an admin(")


# Getting a statistic from a database
async def get_statistic(message: types.Message):
    await message.answer(f"Statistic ⮟"
                         f"\nCount of users: {count_users()}"
                         f"\nName os users: {name_users()}")


def list_handlers_admin(dp):
    dp.register_message_handler(check_admin, commands=['admin_on'])
    dp.register_message_handler(get_statistic, commands=['admin_rights'])
