import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def approve_join(req: types.ChatJoinRequest):
    try:
        await req.approve()
    except Exception as e:
        print("CRITICAL ERROR:", e)

async def safe_polling():
    while True:
        try:
            await bot.polling(
                allowed_updates=types.AllowedUpdates.all(),
                request_timeout=60
            )
        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(3) 

asyncio.run(safe_polling())
