import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
class AutoInsurance(StatesGroup):
    full_name = State()
    phone = State()
    car_model = State()
    car_number = State()
    menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚗 Avto sug'urta"), KeyboardButton(text="✈️ Sayohat sug'urtasi")],
        [KeyboardButton(text="🏠 Mol-mulk sug'urtasi"), KeyboardButton(text="⚠️ Baxtsiz hodisalardan ehtiyot shart sug'urtasi")],
        [KeyboardButton(text="🏃 Sportchilar sug'urtasi"), KeyboardButton(text="🚜 Qishloq xo'jaligi sug'urtasi")],
        [KeyboardButton(text="🏭 Korxona sug'urtasi"), KeyboardButton(text="📄 Mening arizalarim")],
        [KeyboardButton(text="📍 Filiallar"), KeyboardButton(text="☎️ Operator bilan bog'lanish")],
        [KeyboardButton(text="ℹ️ Biz haqimizda")],
    ],
    resize_keyboard=True
)

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True
    )
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Apex Insurance botiga xush kelibsiz!\n\n"
        "Kerakli xizmatni tanlang:",
        reply_markup=menu
)
