from dotenv import load_dotenv

import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Logging
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


# Initialize environment variables
load_dotenv('/home/elizabeth/telegram_bot/.env')


# Initialize bot and dispatcher
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


# Initialize DataBase
host = os.getenv("HOST")
user_db = os.getenv("DB_USER")
user_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")


# Initialize client for keyboard
trouble = KeyboardButton('/I_have_a_little_problem_😝')
key_trouble = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


# Initialize client for inline_keyboard
lang_guide = InlineKeyboardMarkup(row_width=1)
index = ["en", "uk", "es", "de", "pl", "sv"]
lang_en = InlineKeyboardButton(text="English", callback_data="en")
lang_ua = InlineKeyboardButton(text="Ukrainian", callback_data="uk")
lang_es = InlineKeyboardButton(text="Spanish", callback_data="es")
lang_de = InlineKeyboardButton(text="German", callback_data="de")
lang_pl = InlineKeyboardButton(text="Polish", callback_data="pl")
lang_se = InlineKeyboardButton(text="Swedish", callback_data="sv")

key_ex = InlineKeyboardMarkup(row_width=1)
examples = InlineKeyboardButton(text="How to use it 🧐", callback_data="get_example")

# Admin
admin_id = int(os.getenv("ADMIN_ID"))


# Links
git_hub = 'https://github.com/Neliz3/telegram_bot'
