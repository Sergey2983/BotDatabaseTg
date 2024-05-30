
from aiogram import Dispatcher, Bot, types, executor
from database.database import initialize_db, add_user, get_user

API_TOKEN = '7301310155:AAHOJxiUhyib2Zya1in4VbjfOs_rqgUZ52Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.reply('hi')
    else:
        await message.reply('hi')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)