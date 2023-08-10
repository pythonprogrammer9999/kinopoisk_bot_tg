from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from handler.films_command import get_random_movie_by_genre, get_best_movies_by_genres, get_random_movie
from keyboards import kb_client
from keyboards.client_kb import choice_genres, kb_main_menu


class FSMMenu(StatesGroup):
    FSMCategory = State()
    FSMGenre = State()
    FSMMore_films = State()


page = 1


async def start_handler(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выбери категорию', reply_markup=kb_client)
        await FSMMenu.FSMCategory.set()
        await message.delete()
    except:
        await message.reply('Общение с ботом на прямую, напишите ему: https://t.me/FilmsBeeest_bot')


async def choice_category(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['FSMCategory'] = message.text
    if data['FSMCategory'] == 'Случайный фильм':
        await get_random_movie(message)
        await message.reply('Приятного просмотра!', reply_markup=kb_main_menu)
        await FSMMenu.FSMMore_films.set()
    else:
        await FSMMenu.next()
        await message.reply('выберите жанр', reply_markup=choice_genres)


async def choice_genre(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['FSMGenre'] = message.text
    if data['FSMCategory'] == 'Случайные фильмы по жанрам':
        await get_random_movie_by_genre(message, data['FSMGenre'])
        await message.reply('Приятного просмотра!', reply_markup=kb_main_menu)
        await FSMMenu.next()
    if data['FSMCategory'] == 'Лучшие фильмы по жанрам':
        await get_best_movies_by_genres(message, data['FSMGenre'])
        await message.reply('Приятного просмотра!', reply_markup=kb_main_menu)
        await FSMMenu.next()


async def repeated_search(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['FSMMore_films'] = message.text
    if data['FSMMore_films'] == '/Меню':
        await state.finish()
        await start_handler(message)

    if data['FSMCategory'] == 'Лучшие фильмы по жанрам':
        if data['FSMMore_films'] == 'Еще!':
            global page
            page += 1
            await get_best_movies_by_genres(message, data['FSMGenre'], page)

    if data['FSMCategory'] == 'Случайные фильмы по жанрам':
        if data['FSMMore_films'] == 'Еще!':
            await get_random_movie_by_genre(message, data['FSMGenre'])
            await message.reply('Приятного просмотра!', reply_markup=kb_main_menu)

    if data['FSMCategory'] == 'Случайный фильм':
        if data['FSMMore_films'] == 'Еще!':
            await get_random_movie(message)
            await message.reply('Приятного просмотра!', reply_markup=kb_main_menu)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help', 'Меню'], state=None)
    dp.register_message_handler(choice_category, state=FSMMenu.FSMCategory)
    dp.register_message_handler(choice_genre, state=FSMMenu.FSMGenre)
    dp.register_message_handler(repeated_search, state=FSMMenu.FSMMore_films)
