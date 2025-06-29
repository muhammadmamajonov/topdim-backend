from credentials import get_credentials
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

credentials = get_credentials()

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(credentials.TOKEN)

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()