from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

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
    car_year = State()
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚗 Avto sug'urta")],
        [KeyboardButton(text="✈️ Sayohat sug'urtasi")],
        [KeyboardButton(text="🏥 Tibbiy sug'urta")],
        [KeyboardButton(text="📞 Bog'lanish"),
         KeyboardButton(text="ℹ️ Biz haqimizda")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Apex Insurance botiga xush kelibsiz.\n\n"
        "Quyidagi xizmatlardan birini tanlang:",
        reply_markup=menu
    )
phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True
)

@dp.message(lambda message: message.text == "🚗 Avto sug'urta")
async def auto(message: Message):
    await message.answer(
        "🚗 Avto sug'urta bo'limi.\n\n"
        "Tez orada bu yerda sug'urta rasmiylashtirish xizmati mavjud bo'ladi."
    )


@dp.message(lambda message: message.text == "✈️ Sayohat sug'urtasi")
async def travel(message: Message):
    await message.answer(
        "✈️ Sayohat sug'urtasi bo'limi."
    )


@dp.message(lambda message: message.text == "🏥 Tibbiy sug'urta")
async def medical(message: Message):
    await message.answer(
        "🏥 Tibbiy sug'urta bo'limi."
    )


@dp.message(lambda message: message.text == "📞 Bog'lanish")
async def contact(message: Message):
    await message.answer(
        "📞 Telefon: +998 88 272 70 73"
    )


@dp.message(lambda message: message.text == "ℹ️ Biz haqimizda")
async def about(message: Message):
    await message.answer(
        "Apex Insurance — ishonchli sug'urta xizmatlari."
    )


async def main():
    print("✅ Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
