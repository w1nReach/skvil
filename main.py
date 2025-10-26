import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MIN_DELAY = 10        # минимальная задержка перед одобрением (изменяем под себя *но эта задержка рекомендуется)
MAX_JITTER = 3        # + случайная задержка до 3 сек (для естественности)

@dp.chat_join_request_handler()
async def approve_join(req: types.ChatJoinRequest):
    await asyncio.sleep(MIN_DELAY + (asyncio.get_event_loop().time() % MAX_JITTER))
    try:
        await req.approve()
    except:

async def main():
    while True:
        try:
            await dp.start_polling()
        except:
            await asyncio.sleep(5) 

if __name__ == '__main__':
    asyncio.run(main())
