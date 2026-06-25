import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ضع التوكن الخاص بك هنا
TOKEN = "8820864073:AAHFvZO_qP4KI9NJSvryeEgLb1ZccpGvAqs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ البوت يعمل بنجاح على Render!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
