from aiogram import Bot, Dispatcher, Router

from config import BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(BOT_TOKEN, parse_mode="HTML")

# Dispatcher is a root router
dp = Dispatcher()
# ... and all other routers should be attached to Dispatcher
dp.include_router(router)
