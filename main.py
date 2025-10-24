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

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
