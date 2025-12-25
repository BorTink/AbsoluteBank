from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_first = InlineKeyboardMarkup()
start_first_1 = InlineKeyboardButton(
    'Начать', callback_data='Начать'
)
start_first.add(start_first_1)


variants_1 = InlineKeyboardButton(
    'А', callback_data='А'
)
variants_2 = InlineKeyboardButton(
    'Б', callback_data='Б'
)
variants_3 = InlineKeyboardButton(
    'В', callback_data='В'
)
variants_4 = InlineKeyboardButton(
    'Г', callback_data='Г'
)

variants = InlineKeyboardMarkup()
variants.add(variants_1, variants_2, variants_3)

variants_second = InlineKeyboardMarkup()
variants_second.add(variants_1, variants_2)

variants_third = InlineKeyboardMarkup()
variants_third.add(variants_1, variants_2).add(variants_3, variants_4)

da = InlineKeyboardMarkup()
da_1 = InlineKeyboardButton(
    'Да, все правильно', callback_data='ДА'
)
da.add(da_1)
