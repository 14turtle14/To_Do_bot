import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import settings
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

dp = Dispatcher()
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
days_of_week = {i: [] for i in days}


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, I'm To Do bot, here you can make a schedule for the week, leave some global goals")


@dp.message(Command("mn"))
async def show_monday_schedule(message: Message):
    text = "*Понедельник*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["MONDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("ts"))
async def show_tuesday_schedule(message: Message):
    text = "*Вторник*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["TUESDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("wd"))
async def show_wednesday_schedule(message: Message):
    text = "*Среда*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["WEDNESDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("th"))
async def show_thursday_schedule(message: Message):
    text = "*Четверг*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["THURSDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("fr"))
async def show_friday_schedule(message: Message):
    text = "*Пятница*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["FRIDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("st"))
async def show_saturday_schedule(message: Message):
    text = "*Суббота*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["SATURDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message(Command("sn"))
async def show_sunday_schedule(message: Message):
    text = "*Воскресенье*:\n"
    text += "-".join(f"- {i}\n" for i in days_of_week["SUNDAY"])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


b1 = KeyboardButton(text='Понедельник')
b2 = KeyboardButton(text='Вторник')
b3 = KeyboardButton(text='Среда')
b4 = KeyboardButton(text='Четверг')
b5 = KeyboardButton(text='Пятница')
b6 = KeyboardButton(text='Суббота')
b7 = KeyboardButton(text='Воскресенье')
@dp.message(Command("help"))
async def help_info(message: Message):
    text = "If u have problems with bot, send the message to "


keybord_buttons = [[b1, b2, b3, b4, b5, b6, b7]]
keyboard = ReplyKeyboardMarkup(keyboard=keybord_buttons, resize_keyboard=True)
@dp.message(Command("all"))
async def show_all_schedule(message: Message):
    await show_monday_schedule(message)
    await show_tuesday_schedule(message)
    await show_wednesday_schedule(message)
    await show_thursday_schedule(message)
    await show_friday_schedule(message)
    await show_saturday_schedule(message)
    await show_sunday_schedule(message)

@dp.message(Command("add"))
async def add_to_schedule(message: Message):
    await message.answer("Choose the day", reply_markup=keyboard)



async def main():
    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())