import asyncio
import os
from aiogram import Bot, types, Dispatcher 


API_TOKEN = os.getenv("7951258588:AAHxgaubHfJb01xcyd95HakpLIj1ierIezQ")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Обробник команд
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
        await message.reply("Бот для коментарів активний!")

# Обробник коментарів
@dp.message_handler()
async def echo_message(msg: types.Message):
        await bot.send_message(msg.from_user.id, msg.text)
async def main():
        await dp.start_polling(bot)

        if __name__ == "__main__":
            asyncio.run(main())