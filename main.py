import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import settings

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


@dp.message(Command("all"))
async def show_all_schedule(message: Message):
    pass


async def main():
    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())