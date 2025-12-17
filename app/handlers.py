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

ADMIN_CHAT_ID = -5065315574

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


QR_MAP = {
    'eignbjs': 'qr_1',
    'cbdjemf': 'qr_2',
    'lvmrewt': 'qr_3',
    'gkrnejf': 'qr_4',
    'grewgwd': 'qr_5',
    'vsdqfgg': 'qr_6',
    'bbsawer': 'qr_7',
}


# <<---------------------------------------Регистрация----------------------------------------------------------->>

async def final_answer(message, state):
    count = await get_info_from_state(state, 'count')
    if not count:
        count = 0
    if count >= 7:
        message.answer(
            'Поздравляем Вас с успешным прохождением квеста. Спасибо за участие! '
            'Забирайте выигранные жетоны у эльфа на информационной стойке в пункте проката.'
        )
    else:
        await add_info_to_state(state, 'count', count + 1)


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

    if entry == 'qr_1':
        team = await dal.Teams.get_team_by_captain_id(user_id)
        if team:
            await message.answer(
                f'Вы уже создали команду с названием {team["team_name"]}'
            )
        else:
            await message.answer(
                'Укажите ФИО:'
            )
            await state.set_state('Укажите ФИО')
    elif entry == 'qr_2':
        await message.answer(
            'Вам предстоит прослушать аудиозапись, в которой слова звучат наоборот. '
            'Ваша задача разгадать, какие слова были перевернуты.',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 2 - старт')
    elif entry == 'qr_3':
        await message.answer(
            'Задание для самых внимательных! Перед вами расположена последовательность букв. '
            'Ваша задача — найти в ней 5 слов, связанных с Абсолют Банком, '
            'и отправить все найденные слова в этот чат-бот одним сообщением через запятую c пробелом. '
            'Будьте внимательны и не спешите!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 3 - старт')
    elif entry == 'qr_4':
        await message.answer(
            'Мы зашифровали зимние фразы с помощью шифра Цезаря (сдвиг +2)!  '
            'Ваша миссия — разгадать каждую зашифрованную строку и отправить '
            'правильные фразы в этот чат-бот одним сообщением! '
            'За каждую правильно расшифрованную фразу вы получите по 5 баллов!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 4 - старт')
    elif entry == 'qr_5':
        await message.answer(
            'Мы изучили историю логотипа Абсолют Банка. '
            'Ваша задача — определить тот логотип, который не является логотипом банком!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 5 - старт')
    elif entry == 'qr_6':
        await message.answer(
            'Новый год – это время для подведения итогов, время оглянуться назад и оценить пройденный путь. '
            'Это момент, когда особенно важно сказать коллегам тёплые слова '
            'благодарности за совместную работу, за взаимовыручку и поддержку, за тот вклад, '
            'который каждый внес в общий успех. Ведь именно благодаря сплоченной команде, '
            'взаимопониманию и профессионализму мы достигли результатов, которыми можем гордиться. '
            'Напишите коллеге благодарность за совместную работу в любом мессенджере '
            'и отправьте скриншот сообщения в чат-бот.',
        )
    elif entry == 'qr_7':
        await message.answer(
            'Перед вами новостные заголовки с упоминанием Абсолют банка. '
            'Ваша задача — вставить пропущенные слова и отправить вариант ответа в чат-бот!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 7 - старт')
    else:
        team = await dal.Teams.get_team_by_captain_id(user_id)
        if team:
            await message.answer(
                f'Вы уже создали команду с названием {team["team_name"]}'
            )
        else:
            await message.answer(
                'Укажите ФИО:'
            )
            await state.set_state('Укажите ФИО')


@dp.message_handler(state='Укажите ФИО')
async def fio(message: types.Message, state: FSMContext):
    fio = message.text
    await add_info_to_state(state, 'fio', fio)
    await message.answer(
        'Укажите контактный номер телефона:'
    )
    await state.set_state('Укажите контактный номер телефона')


@dp.message_handler(state='Укажите контактный номер телефона')
async def phone(message: types.Message, state: FSMContext):
    phone = message.text
    await add_info_to_state(state, 'phone', phone)

    fio = await get_info_from_state(state, 'fio')

    team = await dal.Teams.get_team_by_name(f"{fio} --- {phone}")
    if team:
        await message.answer(
            f'Вы уже регистрировались.'
        )
    else:
        await dal.Teams.create_team(message.from_user.id, f"{fio} --- {phone}")
        await message.answer(
            f'Мы приветствуем Вас на этапе «Новогодняя открытка». '
            f'Ваша задача повторить любое фото из коллажа на выбор как можно точнее!',
            reply_markup=kb.start_first
        )
        await state.set_state('Задание 1 - старт')


# <<---------------------------------------Задание 1----------------------------------------------------------->>


@dp.callback_query_handler(state='Задание 1 - старт', text='Начать')
async def task_1(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'Фотодобыча' / 'Новогодняя открытка.jpg'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 1 - ожидание фото')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 1 - ожидание фото')
async def handle_photo(message: types.Message, state: FSMContext):
    team = await dal.Teams.get_team_by_captain_id(message.from_user.id)
    await message.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=message.photo[-1].file_id,
        caption=f'Фото от пользователя {team["team_name"]}'
    )

    await message.answer(
        'Отлично, фотография отправлена администратору на проверку! '
        'Ищите следующий QR-код.'
    )

    await state.set_state('Задание 1 - закончил')
    await final_answer(message, state)


# <<---------------------------------------Задание 2----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 2 - старт', text='Начать')
async def task_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Вам предстоит прослушать аудиозапись, в которой слова звучат наоборот. '
        'Ваша задача разгадать, какие слова были перевернуты.'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'Наоборот' / 'Наоборот_1.mp3'

    with open(audio_path, 'rb') as audio:
        await callback.message.answer_audio(audio)

    await state.set_state('Задание 2 - аудио 1 - ожидание')


@dp.message_handler(state='Задание 2 - аудио 1 - ожидание')
async def task_2__answer_1(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'каток':
        await message.answer('Вы абсолютно правы, это КАТОК! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ КАТОК. '
            'Переходим к следующему вопросу.'
        )

    await message.answer(
        'Прослушайте аудиозапись и назовите слово, которое звучит наоборот'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'Наоборот' / 'Наоборот_2.mp3'

    with open(audio_path, 'rb') as audio:
        await message.answer_audio(audio)

    await state.set_state('Задание 2 - аудио 2 - ожидание')


@dp.message_handler(state='Задание 2 - аудио 2 - ожидание')
async def task_2__answer_2(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'новый год':
        await message.answer('Вы абсолютно правы, это НОВЫЙ ГОД! Переходим к следующему вопросу.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ НОВЫЙ ГОД. '
            'Переходим к следующему вопросу.'
        )

    await message.answer(
        'Прослушайте аудиозапись и назовите слово, которое звучит наоборот'
    )

    audio_path = Path(__file__).resolve().parents[1] / 'Наоборот' / 'Наоборот_3.mp3'

    with open(audio_path, 'rb') as audio:
        await message.answer_audio(audio)

    await state.set_state('Задание 2 - аудио 3 - ожидание')


@dp.message_handler(state='Задание 2 - аудио 3 - ожидание')
async def task_2__answer_3(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'чудеса':
        await message.answer('Вы абсолютно правы, это ЧУДЕСА! Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ, правильный ответ ЧУДЕСА. '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 2 - закончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 3----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 3 - старт', text='Начать')
async def task_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Последовательность букв: \n'
        'ГПРЗАБСОЛЮТКНГТАВТОКРЕДИТЛМНБИПОТЕКАСРТЮСТРАХОВАНИЕВШГАРАНТИЯКСЧ'
    )

    await state.set_state('Задание 3 - ожидание')


@dp.message_handler(state='Задание 3 - ожидание')
async def task_3__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    answer = answer.split(', ')
    right_answers = ['гарантия', 'абсолют', 'автокредит', 'ипотека', 'страхование']

    increase = 0
    for a in right_answers:
        if a in answer:
            increase += 2
    await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", increase)

    text_with_answers = ('ГПРЗ<b>АБСОЛЮТ</b>КНГТ<b>АВТОКРЕДИТ</b>ЛМНБ<b>ИПОТЕКА'
                         '</b>СРТЮ<b>СТРАХОВАНИЕ</b>ВШ<b>ГАРАНТИЯ</b>КСЧ')

    if increase == 10:
        await message.answer(
            f'Вы абсолютно правы! {text_with_answers} Ищите следующий QR-код.',
            parse_mode='HTML'
        )
    else:
        await message.answer(
            f'К сожалению, не все ответы были даны верно. '
            f'Здесь выделены все спрятанные слова {text_with_answers}. Ищите следующий QR-код.',
            parse_mode='HTML'
        )

    await state.set_state('Задание 3 - окончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 4----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 4 - старт', text='Начать')
async def task_4(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'прдрерёпжж щхёр'
    )

    await state.set_state('Задание 4 - текст 1 - ожидание')


@dp.message_handler(state='Задание 4 - текст 1 - ожидание')
async def task_4__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'новогоднее чудо':
        await message.answer('Вы абсолютно правы! Правильный ответ: Новогоднее чудо. Переходим к следующему заданию.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, ответ неверный. Правильный ответ: Новогоднее чудо. '
            'Переходим к следующему заданию.'
        )

    await message.answer(
        'упжипэл цжуф'
    )

    await state.set_state('Задание 4 - текст 2 - ожидание')


@dp.message_handler(state='Задание 4 - текст 2 - ожидание')
async def task_4__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'снежный фест':
        await message.answer('Вы абсолютно правы! Правильный ответ: Снежный фест. Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, ответ неверный. Правильный ответ: Снежный фест. '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 4 - окончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 5----------------------------------------------------------->>

@dp.callback_query_handler(state='Задание 5 - старт', text='Начать')
async def task_5(callback: types.CallbackQuery, state: FSMContext):
    photo_path = Path(__file__).resolve().parents[1] / 'ЛОГОТИП' / 'ЛОГОТИП.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await state.set_state('Задание 5 - ожидание')


@dp.message_handler(state='Задание 5 - ожидание')
async def task_5__answer(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == '2':
        await message.answer('Вы абсолютно правы! Ищите следующий QR-код')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: 2. '
            'Ищите следующий QR-код'
        )

    await state.set_state('Задание 4 - окончил')

    await final_answer(message, state)


# <<---------------------------------------Задание 6----------------------------------------------------------->>

@dp.message_handler(content_types=types.ContentType.PHOTO, state='Задание 6 - старт')
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
    photo_path = Path(__file__).resolve().parents[1] / 'Вот это новости' / 'Вот это новости_1.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await callback.message.answer(
        'Варианты ответов:\n'
        '1.	Retail Banking\n'
        '2.	Consumer Finance\n'
        '3.	Retail Finance\n'
        '4.	Financial Retail',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - фото 1 - ожидание')


@dp.callback_query_handler(state='Задание 7 - фото 1 - ожидание')
async def task_7__answer__1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == '3':
        await callback.message.answer('Вы абсолютно правы! Переходим к следующему заданию.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: 3. '
            'Переходим к следующему заданию.'
        )

    photo_path = Path(__file__).resolve().parents[1] / 'Вот это новости' / 'Вот это новости_2.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await callback.message.answer(
        'Варианты ответов:\n'
        '1.	Топ-3\n'
        '2.	Топ-6\n'
        '3.	Топ-5\n'
        '4.	Топ-10',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - фото 2 - ожидание')


@dp.callback_query_handler(state='Задание 7 - фото 2 - ожидание')
async def task_7__answer__2(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == '2':
        await callback.message.answer('Вы абсолютно правы! Переходим к следующему заданию.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: 2. '
            'Переходим к следующему заданию.'
        )

    photo_path = Path(__file__).resolve().parents[1] / 'Вот это новости' / 'Вот это новости_2.png'

    with open(photo_path, 'rb') as photo:
        await callback.message.answer_photo(photo)

    await callback.message.answer(
        'Варианты ответов:\n'
        '1.	любимых\n'
        '2.	частных\n'
        '3.	финансовых\n'
        '4.	ипотечных',
        reply_markup=kb.variants
    )

    await state.set_state('Задание 7 - фото 3 - ожидание')


@dp.callback_query_handler(state='Задание 7 - фото 3 - ожидание')
async def task_7__answer__3(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    if answer == '4':
        await callback.message.answer('Вы абсолютно правы! Ищите следующий QR-код.')
        await dal.Teams.increase_score_by_name(f"{fio} --- {phone}", 5)
    else:
        await callback.message.answer(
            'К сожалению, это неверный ответ. Правильный ответ: 4. '
            'Ищите следующий QR-код.'
        )

    await state.set_state('Задание 7 - закончил')

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



