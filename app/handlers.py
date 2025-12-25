import os
from pathlib import Path

from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from dotenv import load_dotenv

import dal
from utils import add_info_to_state, get_info_from_state
import app.keyboards as kb

load_dotenv()
bot = Bot(os.getenv('TOKEN'))

ADMIN_CHAT_ID = -5243715700

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

QR_MAP = {
    'eignbjs': 'qr_1',
    'grejife': 'qr_2',
    'fwejior': 'qr_3',
    'fjreiog': 'qr_4',
    'fkoekvf': 'qr_5',
    'wqpokff': 'qr_6',
    'poemvkr': 'qr_7',
    'feopjwf': 'qr_8',
    'dmksgjr': 'qr_9',
    'cmrjgiw': 'qr_10',
    'tiorepw': 'qr_11',
    'mqwkmbr': 'qr_12',
    'qjieowo': 'qr_13',
    'efkorpt': 'qr_14',
    'bmioerg': 'qr_15',
    'qopkvre': 'qr_16',
    'qeojpor': 'qr_17',
    'qoimvoi': 'qr_18',
    'wjirgwo': 'qr_19',
    'egqkopr': 'qr_20',
    'jriwoev': 'qr_21',
}


# <<---------------------------------------Регистрация----------------------------------------------------------->>

async def final_answer(message, state):
    count = await get_info_from_state(state, 'count')
    if not count:
        count = 0
    if count >= 17:
        message.answer(
            'Поздравляем Вас с успешным прохождением квеста. Спасибо за участие! '
            'Забирайте выигранные жетоны у эльфа на информационной стойке в пункте проката.'
        )
    else:
        await add_info_to_state(state, 'count', count + 1)


async def choose_task(user_id, entry, message, state):
    if entry == 'qr_1':
        await message.answer(
            'Мы приветствуем Вас на станции «Новогодний фото-челлендж». '
            'В этом задании вам понадобятся юмор, креативный подход и смекалка. '
            'Сделайте наиболее точные копии фотографий, которые мы вам отправим. '
            'Готовые фото отправляйте в чат на проверку.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 1 - старт')
    elif entry == 'qr_2':
        await message.answer(
            'Придумайте и напишите в чат короткий новогодний тост или пожелание, используя три обязательных слова:\n'
            'КОМАНДА\n'
            'ПОЕЗД\n'
            'ПРАЗДНИК\n\n'
            'Можете добавить свои слова и эмоции! Креативность приветствуется! '
            'Готовое пожелание отправляйте в чат на проверку.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 2 - старт')
    elif entry == 'qr_3':
        await message.answer(
            'В таблице букв найдите 5 слов, связанных с Новым годом! '
            'Слова расположены по горизонтали. Пишите слова с маленькой буквы через запятую.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 3 - старт')
    elif entry == 'qr_4':
        await message.answer(
            'Прослушайте фрагмент новогодней песни (без слов, только мелодия) и угадайте её название. '
            'Необходимо отправить именно название песни в чат! '
            'Желаем Вам удачи на станции музыки!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 4 - старт')
    elif entry == 'qr_5':
        await message.answer(
            'Мы зашифровали фразу с помощью шифра Цезаря (шаг +1). '
            'Разгадайте фразу и отправьте ее в чат-бот!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 5 - старт')
    elif entry == 'qr_6':
        await message.answer(
            'Новый год – это время для подведения итогов, время оглянуться назад и оценить пройденный путь. '
            'Это момент, когда особенно важно сказать коллегам тёплые слова благодарности за совместную работу, '
            'за взаимовыручку и поддержку, за тот вклад, который каждый внес в общий успех. '
            'Ведь именно благодаря сплоченной команде, взаимопониманию и профессионализму мы достигли результатов, '
            'которыми можем гордиться.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 6 - старт')
    elif entry == 'qr_7':
        await message.answer(
            'Ответьте на 3 вопроса о новогодних традициях разных стран. Отправьте ответы в чат-бот. Желаем Удачи!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 7 - старт')
    elif entry == 'qr_8':
        await message.answer(
            'Вам предстоит прослушать аудиозапись, в которой слово будет звучать наоборот. '
            'Ваша задача разгадать, какое слово было перевернуто.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 8 - старт')
    elif entry == 'qr_9':
        await message.answer(
            'Разгадайте ребус. Получившееся слово отправьте в чат-бот.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 9 - старт')
    elif entry == 'qr_10':
        await message.answer(
            'Поезда спрятались в зимнем пейзаже. Найдите все составы. В поле для ответа введите одно число.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 10 - старт')
    elif entry == 'qr_11':
        await message.answer(
            'В этом задании вам нужно определить, является ли факт о поездах мифом или правдой.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 11 - старт')
    elif entry == 'qr_12':
        await message.answer(
            'Вспомним школу. Решите логическую задачку про поезда.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 12 - старт')
    elif entry == 'qr_13':
        await message.answer(
            'Все мы любим новогодние фильмы. '
            'Сможете ли вы угадать название фильма, сюжет которого зашифрован с помощью эмодзи?',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 13 - старт')
    elif entry == 'qr_14':
        await message.answer(
            'Перед вами — текст из песни популярного исполнителя, '
            'но его смысл намеренно перевёрнут. '
            'Все строки и образы заменены на противоположные по смыслу. '
            'Ваша задача назвать исполнителя этой песни в формате имя фамилия.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 14 - старт')
    elif entry == 'qr_15':
        await message.answer(
            'Сделайте фото с коллегой, чье имя начинается на букву «К»'
        )
        await state.set_state('Задание 15 - старт')
    elif entry == 'qr_16':
        await message.answer(
            'Сделайте фото с логотипом Capital Group.'
        )
        await state.set_state('Задание 16 - старт')
    elif entry == 'qr_17':
        await message.answer(
            'Наш экспресс мчится сквозь зимние чудеса, а иногда мы путешествуем совсем рядом — по московскому метро. '
            'Ведь метро — это тоже поезд, только под землёй!  '
            'Давайте проверим, насколько хорошо вы знаете московское метро.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 17 - старт')
    else:
        team = await dal.Teams.get_team_by_captain_id(user_id)
        if team:
            pass
        else:
            await message.answer(
                'Добро пожаловать на борт «Новогоднего Экспресса»! '
                'Наш поезд мчит вас сквозь снежные вихри, огни гирлянд и волшебство праздника. '
                'Ваша задача — пройти все станции-испытания, разгадать. '
                'Регистрируйтесь, сканируйте первый QR-код — и вперёд, к приключениям!:'
            )
            await message.answer(
                'Укажите ФИО:'
            )
            await state.set_state('Укажите ФИО')


@dp.message_handler(state='*', commands=['start'])
async def start(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    if user_id == ADMIN_CHAT_ID:
        await message.answer(
            'АДМИН ПАНЕЛЬ: добро пожаловать!'
        )
        await message.answer(
            '1) Чтобы ввести вопрос, введите его без ответа на мое сообщение\n'
            '2) Чтобы выставить баллы за конкретный ответ, '
            'введите число начисляемых баллов в ответ на сообщение с ответом команды'
        )
        await state.set_state('Админ Панель')
        return

    start_arg = (message.get_args() or '').strip()
    entry = QR_MAP.get(start_arg)
    await add_info_to_state(state, 'qr', entry)

    team = await dal.Teams.get_team_by_captain_id(user_id)
    if team:
        await choose_task(user_id, entry, message, state)
    else:
        await message.answer(
            'Добро пожаловать на борт «Новогоднего Экспресса»! '
            'Наш поезд мчит вас сквозь снежные вихри, огни гирлянд и волшебство праздника. '
            'Ваша задача — пройти все станции-испытания, разгадать. '
            'Регистрируйтесь, сканируйте первый QR-код — и вперёд, к приключениям!:'
        )
        await message.answer(
            'Укажите ФИО:'
        )
        await state.set_state('Укажите ФИО')



#
# @dp.message_handler(state='Укажите ФИО')
# async def fio(message: types.Message, state: FSMContext):
#     fio = message.text
#     await add_info_to_state(state, 'fio', fio)
#     await message.answer(
#         'Укажите контактный номер телефона:'
#     )
#     await state.set_state('Укажите контактный номер телефона')


@dp.message_handler(state='Укажите ФИО')
async def fio(message: types.Message, state: FSMContext):
    fio = message.text

    team = await dal.Teams.get_team_by_name(f"{fio}")
    if team:
        await message.answer(
            f'Вы уже регистрировались.'
        )
    else:
        await dal.Teams.create_team(message.from_user.id, f"{fio}")
        await message.answer(
            f'Отлично, тогда можем начинать! Помните, что проходить задания можно в любом порядке'
        )
        await state.set_state('Ожидание заданий')


# <<---------------------------------------Задание 1----------------------------------------------------------->>


@dp.callback_query_handler(state='Задание 1 - старт', text='Начать')
async def task_1(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'Новогодний фоточелендж' / 'фото_1.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 1 - ожидание фото - 1')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 1 - ожидание фото - 1')
async def handle_photo(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'Фото от пользователя {team["team_name"]}'
    )

    await message.answer(
        'Отлично! Переходим к следующей фотографии.'
    )

    photo_path = Path(__file__).resolve().parents[1] / 'Новогодний фоточелендж' / 'фото_2.png'

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo)

    await state.set_state('Задание 1 - ожидание фото - 2')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 1 - ожидание фото - 2')
async def handle_photo(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'Фото от пользователя {team["team_name"]}'
    )

    await message.answer(
        'Отлично! Ищите следующий QR-код.'
    )

    await state.set_state('Задание 1 - закончил')
    await final_answer(message, state)


# <<---------------------------------------Задание 2----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 2 - старт', text='Начать')
async def task_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Введите тост'
    )

    await state.set_state('Задание 2 - ожидание')


@dp.message_handler(state='Задание 2 - ожидание')
async def task_2__text(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f'Задание 2 - тост - ответ от пользователя {team}\n\n {message.text}'
    )

    await message.answer(
        'Отлично! Ищите следующий QR-код.'
    )

    await state.set_state('Задание 2 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 3----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 3 - старт', text='Начать')
async def task_3(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'Найди слова' / 'Найди слова_1.jpg'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 3 - ожидание')


@dp.message_handler(state='Задание 3 - ожидание')
async def task_3__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    answer = answer.split(', ')
    right_answers = ['успех', 'праздник', 'цель', 'счастье', 'радость', 'единство']

    increase_amount = 2
    increase = 0
    for a in right_answers:
        if a in answer:
            increase += increase_amount
    await dal.Teams.increase_score_by_name(f"{fio}", increase)

    if increase == increase_amount * 6:
        await message.answer(
            f'Вы абсолютно правы! Ищите следующий QR-код.',
        )
    else:
        await message.answer(
            f'К сожалению, не все ответы были даны верно. '
            f'Здесь выделены все спрятанные слова. Ищите следующий QR-код.',
        )

    photo_path = Path(__file__).resolve().parents[1] / 'Найди слова' / 'Найди слова_2.jpg'

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo)

    await state.set_state('Задание 3 - окончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 4----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 4 - старт', text='Начать')
async def task_4(callback: types.CallbackQuery, state: FSMContext):
    audio_path = Path(__file__).resolve().parents[1] / 'Угадай мелодию' / 'мелодия_1.mp3'

    with open(audio_path, 'rb') as audio:
        await callback.message.answer_audio(audio)

    await state.set_state('Задание 4 - аудио 1 - ожидание')


@dp.message_handler(state='Задание 4 - аудио 1 - ожидание')
async def task_4__answer_1(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'кабы не было зимы':
        await message.answer('Вы абсолютно правы, это "Кабы не было зимы"! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ "Кабы не было зимы". '
            'Переходим к следующему вопросу.'
        )

    await message.answer(
        'Прослушайте аудиозапись и назовите слово, которое звучит наоборот'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'Угадай мелодию' / 'мелодия_2.mp3'

    with open(audio_path, 'rb') as audio:
        await message.answer_audio(audio)

    await state.set_state('Задание 4 - аудио 2 - ожидание')


@dp.message_handler(state='Задание 4 - аудио 2 - ожидание')
async def task_4__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'потолок ледяной':
        await message.answer('Вы абсолютно правы, это "Потолок ледяной"! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ "Потолок ледяной". '
            'Переходим к следующему вопросу.'
        )

    await message.answer(
        'Прослушайте аудиозапись и назовите слово, которое звучит наоборот'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'Угадай мелодию' / 'мелодия_3.mp3'

    with open(audio_path, 'rb') as audio:
        await message.answer_audio(audio)

    await state.set_state('Задание 4 - аудио 3 - ожидание')


@dp.message_handler(state='Задание 4 - аудио 3 - ожидание')
async def task_4__answer_3(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'три белых коня':
        await message.answer('Вы абсолютно правы, это "Три белых коня"! Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ "Три белых коня". '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 4 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 5----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 5 - старт', text='Начать')
async def task_5(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Зашифрованная фраза: <b>ШФЕЁТБ ТМФШБЯУТА</b>',
        parse_mode='HTML'
    )

    await state.set_state('Задание 5 - текст 1 - ожидание')


@dp.message_handler(state='Задание 5 - текст 1 - ожидание')
async def task_5__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'чудеса случаются':
        await message.answer('Вы абсолютно правы! Отлично! Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: “Чудеса случаются”. '
            'Шифр Цeзаря– такой вид шифрования текста, при котором все символы в тексте заменяются символами, '
            'сдвинутыми по алфавиту на постоянное количество позиций. '
            'Например, при сдвиге на 1: буква А заменяется на Б, Б на В и т.д. '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 5 - окончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 6----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 6 - старт', text='Начать')
async def task_6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Напишите коллеге благодарность за совместную работу в любом мессенджере '
        'и отправьте скриншот сообщения в чат-бот.'
    )

    await state.set_state('Задание 6 - ожидание')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 6 - ожидание')
async def task_6__text(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'Фото от пользователя {team}'
    )

    await message.answer(
        'Говорите приятные слова коллегам чаще! Спасибо за участие! '
        'Ищите следующий QR-код.'
    )

    await state.set_state('Задание 6 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 7----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 7 - старт', text='Начать')
async def task_7(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('В какой стране на новый год подают 12 виноградин?')

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Испания\n'
        'Б) Франция\n'
        'В) Португалия',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - ожидание - тест 1')


@dp.callback_query_handler(state='Задание 7 - ожидание - тест 1')
async def task_7__answer__1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'А':
        await callback.message.answer('Вы абсолютно правы, это «Испания»! Переходите к следующему вопросу!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Испания». Переходите к следующему вопросу!'
        )

    await callback.message.answer(
        'В Японии под Новый год принято звонить в колокол 108 раз. Что символизирует это число?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Число дней в году\n'
        'Б) Число горных духов\n'
        'В) Число человеческих пороков, от которых нужно очиститься',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - ожидание - тест 2')


@dp.callback_query_handler(state='Задание 7 - ожидание - тест 2')
async def task_7__answer__2(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'В':
        await callback.message.answer('Вы абсолютно правы, это «Число человеческих пороков, '
                                      'от которых нужно очиститься»! Переходите к следующему вопросу!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, '
            'правильный ответ «Число человеческих пороков, от которых нужно очиститься». '
            'Переходите к следующему вопросу!'
        )

    await callback.message.answer(
        'В какой стране на Новый год разбивают тарелки о двери друзей и родственников на удачу?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Германия\n'
        'Б) Дания\n'
        'В) Китай',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - ожидание - тест 3')


@dp.callback_query_handler(state='Задание 7 - ожидание - тест 3')
async def task_7__answer__2(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'Б':
        await callback.message.answer('Вы абсолютно правы, это «Дания»! Ищите следующий QR-код!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Дания». Ищите следующий QR-код!'
        )

    await state.set_state('Задание 7 - закончил')


# <<---------------------------------------Задание 8----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 8 - старт', text='Начать')
async def task_8(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Прослушайте аудиозапись и назовите слово, которое звучит наоборот')

    audio_path = Path(__file__).resolve().parents[1] / 'наоборот' / 'наоборот_1.MP3'

    with open(audio_path, 'rb') as audio:
        await callback.message.answer_audio(audio)

    await state.set_state('Задание 8 - аудио 1 - ожидание')


@dp.message_handler(state='Задание 8 - аудио 1 - ожидание')
async def task_8__answer_1(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'чудеса':
        await message.answer('Вы абсолютно правы, это «Чудеса»! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Чудеса». Переходим к следующему вопросу.'
        )

    await message.answer(
        'Прослушайте аудиозапись и назовите слово, которое звучит наоборот'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'наоборот' / 'наоборот_2.MP3'

    with open(audio_path, 'rb') as audio:
        await message.answer_audio(audio)

    await state.set_state('Задание 8 - аудио 2 - ожидание')


@dp.message_handler(state='Задание 8 - аудио 2 - ожидание')
async def task_4__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'праздник':
        await message.answer('Вы абсолютно правы, это «Праздник»! Ищите следующий QR-код!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Праздник». Ищите следующий QR-код!'
        )

    await state.set_state('Задание 4 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 9----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 9 - старт', text='Начать')
async def task_9(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Прослушайте аудиозапись и назовите слово, которое звучит наоборот')

    photo_path = Path(__file__).resolve().parents[1] / 'ребус' / 'ребус_1.jpg'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 9 - ожидание')


@dp.message_handler(state='Задание 9 - ожидание')
async def task_9__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'мандарины':
        await message.answer('Вы абсолютно правы! Отлично! Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: Мандарины! Ищите следующий QR-код.'
        )

    await state.set_state('Задание 9 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 10----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 10 - старт', text='Начать')
async def task_10(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'найди поезд' / 'найди поезд.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 10 - ожидание')


@dp.message_handler(state='Задание 10 - ожидание')
async def task_10__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == '6':
        await message.answer('Вы абсолютно правы! Ищите следующий QR-код!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ «6». Ищите следующий QR-код!'
        )

    photo_path = Path(__file__).resolve().parents[1] / 'найди поезд' / 'найди поезд_2.png'

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo)

    await state.set_state('Задание 10 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 11----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 11 - старт', text='Начать')
async def task_11(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Существуют поезда с наклоняемым кузовом. Это тип поезда с механизмом наклона вагонов при повороте, '
        'позволяющим проходить повороты на обычной железной дороге с бо́льшей скоростью '
        'без ощущения дискомфорта пассажирами.'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Правда\n'
        'Б) Миф\n',
        reply_markup=kb.variants_second
    )

    await state.set_state('Задание 11 - ожидание - тест 1')


@dp.callback_query_handler(state='Задание 11 - ожидание - тест 1')
async def task_11__answer__1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'А':
        await callback.message.answer('Вы абсолютно правы, это правда! Ищите следующий QR-код!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, это правда. Ищите следующий QR-код!'
        )

    await state.set_state('Задание 11 - закончил')


# <<---------------------------------------Задание 12----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 12 - старт', text='Начать')
async def task_12(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Скорый поезд вышел из Москвы в Санкт-Петербург и шёл без остановок со скоростью 60 км в час. '
        'Другой поезд вышел ему навстречу из Санкт-Петербурга в Москву '
        'и тоже шёл без остановок со скоростью 40 км в час. '
        'Расстояние между Москвой и Санкт-Петербургом составляет 700 км. '
        'На каком расстоянии будут эти поезда за 1 час до их встречи?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) 100'
        'Б) 60'
        'В) 40'
        'Г) 120',
        reply_markup=kb.variants_third
    )

    await state.set_state('Задание 12 - ожидание - тест 1')


@dp.callback_query_handler(state='Задание 12 - ожидание - тест 1')
async def task_12__answer__1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'А':
        await callback.message.answer('Вы абсолютно правы, 100 км! Ищите следующий QR-код!')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ «100 км». Ищите следующий QR-код!'
        )

    await state.set_state('Задание 12 - закончил')


# <<---------------------------------------Задание 13----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 13 - старт', text='Начать')
async def task_13(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'угадай фильм' / 'Угадай фильм_1.jpg'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 13 - ожидание - тест 1')


@dp.message_handler(state='Задание 13 - ожидание - тест 1')
async def task_13__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '').replace(',', '')
    if answer == 'ирония судьбы или с легким паром':
        await message.answer(
            'Вы абсолютно правы, это «Ирония судьбы, или с легким паром»! Переходим к следующему вопросу.'
        )
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Ирония судьбы, или с легким паром». '
            'Переходим к следующему вопросу.'
        )

    photo_path = Path(__file__).resolve().parents[1] / 'угадай фильм' / 'Угадай фильм_2.jpg'

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo)

    await state.set_state('Задание 13 - ожидание - тест 2')


@dp.message_handler(state='Задание 13 - ожидание - тест 2')
async def task_13__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'девчата':
        await message.answer(
            'Вы абсолютно правы, это фильм «Девчата»! Ищите следующий QR-код!'
        )
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ «Девчата». Ищите следующий QR-код!'
        )

    await state.set_state('Задание 13 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 14----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 14 - старт', text='Начать')
async def task_14(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        '«Не рвутся деревни\n'
        'Ты нигде здесь не жил\n'
        'Их мирили самолеты\n'
        'И ссорил их полный аэропорт\n\n'
        'Чтоб расстаться на время\n'
        'Я позже билеты сдал\n'
        'Их мирили самолеты\n'
        'И ссорил их полный аэропорт'
    )

    await state.set_state('Задание 14 - ожидание')


@dp.message_handler(state='Задание 14 - ожидание')
async def task_14__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower().replace('"', '')
    if answer == 'женя трофимов':
        await message.answer(
            'Вы абсолютно правы, это Женя Трофимов и это песня «Поезда»! '
            'Ищите следующий QR-код!'
        )
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ Женя Трофимов и это песня «Поезда». '
            'Ищите следующий QR-код!'
        )

    await state.set_state('Задание 14 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 15----------------------------------------------------------->>

@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 15 - старт')
async def task_15__text(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'ЗАДАНИЕ 15 -- Фото от пользователя {team}'
    )

    await message.answer(
        'Отлично! Ищите следующий QR-код.'
    )

    await state.set_state('Задание 15 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 16----------------------------------------------------------->>

@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 16 - старт')
async def task_16__text(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'ЗАДАНИЕ 16 -- Фото от пользователя {team}'
    )

    await message.answer(
        'Отлично! Ищите следующий QR-код.'
    )

    await state.set_state('Задание 16 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 17----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 17 - старт', text='Начать')
async def task_12(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Большая кольцевая линия, которую достроили в 2023 году, '
        'считается самой длинной кольцевой линией в мире. '
        'Сколько нужно времени, чтобы проехать полный круг?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) 30 минут\n'
        'Б) 90 минут\n'
        'В) 55 минут\n'
        'Г) 120 минут',
        reply_markup=kb.variants_third
    )

    await state.set_state('Задание 17 - ожидание - тест 1')


@dp.callback_query_handler(state='Задание 17 - ожидание - тест 1')
async def task_12__answer__1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'Б':
        await callback.message.answer('Вы абсолютно правы, 90 минут! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ 90 минут. Переходим к следующему вопросу.'
        )

    await callback.message.answer(
        'В московском метро чего только не увидишь: скульптуры, картины, барельефы, мозаики... '
        'А есть ли там фонтаны?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Да\n'
        'Б) Нет\n',
        reply_markup=kb.variants_second
    )

    await state.set_state('Задание 17 - ожидание - тест 2')


@dp.callback_query_handler(state='Задание 17 - ожидание - тест 2')
async def task_12__answer__2(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'А':
        await callback.message.answer(
            'Вы абсолютно правы, '
            'фонтан находится рядом со станцией «Римская» и выполнен в тематике Древнего Рима! '
            'Переходим к следующему вопросу.'
        )
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ «ДА» '
            'фонтан находится рядом со станцией «Римская» и выполнен в тематике Древнего Рима. '
            'Переходим к следующему вопросу.'
        )

    await callback.message.answer(
        'Всегда ли схема метро была цветной?'
    )

    await callback.message.answer(
        'Варианты ответов:\n'
        'А) Да\n'
        'Б) Нет\n',
        reply_markup=kb.variants_second
    )

    await state.set_state('Задание 17 - ожидание - тест 3')


@dp.callback_query_handler(state='Задание 17 - ожидание - тест 3')
async def task_12__answer__3(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == 'Б':
        await callback.message.answer(
            'Вы абсолютно правы, до 1957 года линии не имели цветного обозначения. '
            'А «разукрасили» их для удобства иностранных туристов — к международному молодёжному фестивалю. '
            'Ищите следующий QR-код.'
        )
        await dal.Teams.increase_score_by_name(f"{fio}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ, правильный ответ «НЕТ». '
            'До 1957 года линии не имели цветного обозначения. '
            'А «разукрасили» их для удобства иностранных туристов — к международному молодёжному фестивалю. '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 17 - закончил')

    await final_answer(callback.message, state)


# <<---------------------------------------Админ панель----------------------------------------------------------->>

@dp.message_handler(state='Админ Панель', commands=['ask'])
async def admin__ask_question(message: types.Message, state: FSMContext):
    if message.chat.id != ADMIN_CHAT_ID:
        return
    print(2)
    question = message.text.replace('/ask ', '')
    if question.isnumeric():
        await message.reply('ОШИБКА: вопрос не должен быть просто числом. Возможно, здесь опечатка')
        return

    teams = await dal.Teams.get_all_teams()
    for team in teams:
        captain_state = dp.current_state(chat=team['captain_id'], user=team['captain_id'])

        await bot.send_message(chat_id=team['captain_id'], text=f"Вопрос: {question}")
        await captain_state.set_state('Задан вопрос')

    await message.reply('Вопрос был успешно задан всем командам')


@dp.message_handler(state='Админ Панель', commands=['scores'])
async def admin__get_scores(message: types.Message, state: FSMContext):
    if message.chat.id != ADMIN_CHAT_ID:
        print(1222)
        return

    print(3)
    teams = await dal.Teams.get_all_teams()
    text = ""
    for team in teams:
        text += f"<b>{team['team_name']}</b> --- {team['score']} баллов\n"

    await message.reply(
        text,
        parse_mode='HTML'
    )


@dp.message_handler(state='Админ Панель')
async def admin__increase_score(message: types.Message, state: FSMContext):
    # Если это ответ на сообщение --> выставление баллов
    if message.reply_to_message:
        print(1)
        score_increase = message.text
        if not score_increase.isnumeric():
            await message.reply('ОШИБКА: введите число')
            return
        score_increase = int(score_increase)

        answer_text = message.reply_to_message.caption
        team_name = answer_text.split('Фото от пользователя ')[-1]

        increased_team = await dal.Teams.increase_score_by_name(team_name, score_increase)
        if not increased_team:
            await message.reply('ОШИБКА: команды не существует')

        team_name = increased_team['team_name']
        new_score = increased_team['score']
        await message.reply(f'Счет пользователя {team_name} был увеличен до {new_score}')
    # else:
    #     print(2)
    #     question = message.text
    #     if question.isnumeric():
    #         await message.reply('ОШИБКА: вопрос не должен быть просто числом. Возможно, здесь опечатка')
    #         return
    #
    #     teams = await dal.Teams.get_all_teams()
    #     for team in teams:
    #         captain_state = dp.current_state(chat=team['captain_id'], user=team['captain_id'])
    #
    #         await bot.send_message(chat_id=team['captain_id'], text=f"Вопрос: {question}")
    #         await captain_state.set_state('Задан вопрос')
    #
    #     await message.reply('Вопрос был успешно задан всем командам')
