from telebot import TeleBot, types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "7458366735:AAH7iqg4Qpvde603zMxHjesgN5n6tHVhC8k"

bot = Bot('7458366735:AAH7iqg4Qpvde603zMxHjesgN5n6tHVhC8k')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    web_app_game = InlineKeyboardButton(text="Play", web_app=WebAppInfo(url='https://markkizik.github.io/IceCube/'))
    tg_channel_btn = InlineKeyboardButton(text="Ice Channel", url='https://t.me/icecubecrypto')
    row_first = [web_app_game]
    row_second = [tg_channel_btn]
    rows = [row_first, row_second]
    markup = types.InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer('Hey it`s Ice Cube🌟', reply_markup=markup)

executor.start_polling(dp)