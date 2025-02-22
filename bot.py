import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8083480689:AAF278fGyn-H_0kelRyLNs2ho3voCAeF7-Q"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://your-app-url.vercel.app"))]],
    resize_keyboard=True
)
    button = KeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://mytelegramapp.vercel.app"))
    keyboard.add(button)

    await message.answer("Нажми на кнопку, чтобы открыть WebApp!", reply_markup=keyboard)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())