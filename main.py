import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# الكود هسة يسحب التوكن من إعدادات السيرفر (Environment Variables)
# يعني ماكو داعي تكتب التوكن هنا، فـ GitHub ماراح يزعجك بعد!
TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ أهلاً بك! البوت الآن يعمل بكامل طاقته على Render.")

@dp.message()
async def echo(message: types.Message):
    # تحويل النص إلى ملف وإرساله
    file_name = "document.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(message.text)
    
    file = types.FSInputFile(file_name)
    await message.reply_document(document=file, caption="📂 هذا ملفك النصي جاهز!")
    
    # حذف الملف بعد الإرسال للحفاظ على مساحة السيرفر
    if os.path.exists(file_name):
        os.remove(file_name)

async def main():
    print("البوت بدأ الآن...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
