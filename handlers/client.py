from aiogram import types, Dispatcher
from create_bot import bot

# @dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Starting')
        await message.delete()
    except:
        await message.reply('For talking with bot text to \nhttps://t.me/Test1MenuBot')

# @dp.message_handler(commands=['working time'])
async def command_working_time(message : types.Message):
    await bot.send_message(message.from_user.id, 'Monday - Friday: 9.00 - 18.00')

# @dp.message_handler(commands=['place'])
async def command_place(message : types.Message):
    await bot.send_message(message.from_user.id, 'Kazakhstan, Shymkent, Kazybek by st., 20/58')


def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_working_time, commands=['working time'])
    dp.register_message_handler(command_place, commands=['place'])

