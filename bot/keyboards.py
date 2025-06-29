from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardButton, InlineKeyboardMarkup, 
    WebAppInfo
)

contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kontaktni jo'natish", request_contact=True)
        ],
    ],
    resize_keyboard=True
)


sayt_link = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ko'rish", web_app=WebAppInfo(url="https://reliable-salmiakki-b79ea8.netlify.app"))]
])