from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_first = InlineKeyboardMarkup()
start_first_1 = InlineKeyboardButton(
    'Начать', callback_data='Начать'
)
start_first.add(start_first_1)


variants = InlineKeyboardMarkup()
variants_1 = InlineKeyboardButton(
    '1', callback_data='1'
)
variants_2 = InlineKeyboardButton(
    '2', callback_data='2'
)
variants_3 = InlineKeyboardButton(
    '3', callback_data='3'
)
variants_4 = InlineKeyboardButton(
    '4', callback_data='4'
)
variants.add(variants_1, variants_2).add(variants_3, variants_4)
