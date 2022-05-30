from time import time

from aiogram import Bot, Dispatcher, executor, types
import logging


API_TOKEN = '5048564633:AAFWa1lKD_s75q__zI06LOdyRFGJvLVMpZo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def bot_start(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['text'])
async def mute(message: types.Message):
    await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,
                                   until_date=time() + 259200)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)