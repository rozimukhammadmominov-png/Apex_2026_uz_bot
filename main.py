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
    @dp.message(AutoInsurance.phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(AutoInsurance.car_model)

    await message.answer(
        "🚘 Avtomobil rusumini kiriting.\n\nMasalan: Cobalt, Gentra, Tracker",
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(AutoInsurance.car_model)
async def get_car_model(message: Message, state: FSMContext):
    await state.update_data(car_model=message.text)
    await state.set_state(AutoInsurance.car_number)

    await message.answer(
        "🔢 Davlat raqamini kiriting.\n\nMasalan: 50 A 123 BC"
    )


@dp.message(AutoInsurance.car_number)
async def get_car_number(message: Message, state: FSMContext):
    await state.update_data(car_number=message.text)

    data = await state.get_data()

    await message.answer(
        f"✅ Arizangiz qabul qilindi!\n\n"
        f"👤 F.I.Sh.: {data['full_name']}\n"
        f"📱 Telefon: {data['phone']}\n"
        f"🚘 Avtomobil: {data['car_model']}\n"
        f"🔢 Davlat raqami: {data['car_number']}\n\n"
        "Operatorimiz tez orada siz bilan bog'lanadi.",
        reply_markup=menu
    )

    await state.clear()
    

async def main():
    print("✅ Bot ishga tushdi")
    await dp.start_polling(bot)

@dp.message(F.text == "🚗 Avto sug'urta")
async def auto_insurance(message: Message, state: FSMContext):
    await state.set_state(AutoInsurance.full_name)
    await message.answer(
        "👤 Iltimos, F.I.Sh. (to'liq ism-familiyangizni) kiriting:",
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(AutoInsurance.full_name)
async def get_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(AutoInsurance.phone)

    await message.answer(
        "📱 Telefon raqamingizni yuboring:",
        reply_markup=phone_keyboard
    )
    
if __name__ == "__main__":
    asyncio.run(main())
