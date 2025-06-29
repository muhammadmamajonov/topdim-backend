from sqlalchemy import select
from .loader import dp, bot
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from .keyboards import contact_keyboard, sayt_link
from aiogram import F
from database import AsyncSessionLocal
from models import User



@dp.message(CommandStart(), F.chat.type == "private")
async def command_start(message: Message):
    await message.answer("Telefon raqamingizni yuboring.", reply_markup=contact_keyboard)


@dp.message(F.contact, F.chat.type == "private")
async def get_contact(message: Message):
    db = AsyncSessionLocal()
    phone = message.contact.phone_number
    user = User(first_name=message.from_user.first_name, last_name=message.from_user.last_name, tg_id=message.from_user.id, phone_number=phone)
    db.add(user)
    await db.commit()
    await db.close()
    await message.answer("Ro'yxatdan o'tdingiz. Endi foydalanishingiz mumkin.", reply_markup=sayt_link)