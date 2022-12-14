import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5984721245:AAHXhaTPh2JzV4R3nBuoEa72G6iDvsm6Mzc")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
