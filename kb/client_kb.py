from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

k1 = KeyboardButton('/place')
k2 = KeyboardButton('/workingtime')
k3 = KeyboardButton('/menu')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(k1).add(k2).add(k3)

