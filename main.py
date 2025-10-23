import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def auto_approve(req: ChatJoinRequest):
    try:
        await req.approve()
    except Exception as e:
        print("CRITICAL ERROR: failed to approve join request ->", e)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print("CRITICAL ERROR: polling stopped ->", e)

if __name__ == "__main__":
    asyncio.run(main())
