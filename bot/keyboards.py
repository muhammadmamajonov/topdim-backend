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
    [InlineKeyboardButton(text="Ko'rish", web_app=WebAppInfo(url="https://73cb-213-230-102-237.ngrok-free.app"))]
])