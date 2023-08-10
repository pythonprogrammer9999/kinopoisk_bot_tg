from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

random_film = KeyboardButton('Случайный фильм')
genres = KeyboardButton('Случайные фильмы по жанрам')
choice = KeyboardButton('Выбрать')
some_films = KeyboardButton('Лучшие фильмы по жанрам')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, )
kb_client.add(random_film, genres, some_films)

#
all_genres = ['аниме', 'биография', 'боевик', 'вестерн', 'военный', \
              'детектив', 'детский', 'для взрослых', 'документальный', \
              'драма', 'игра', 'история', 'комедия', 'концерт', \
              'короткометражка', 'криминал', 'мелодрама', 'музыка', \
              'мультфильм', 'мюзикл', 'новости', 'приключения', \
              'реальное ТВ', 'семейный', 'спорт', 'ток-шоу', 'триллер', \
              'ужасы', 'фантастика', 'фильм-нуар', 'фэнтези', 'церемония']

choice_genres = ReplyKeyboardMarkup(resize_keyboard=True, )

for i in range(len(all_genres)):
    choice_genres.add(all_genres[i])


menu = KeyboardButton('/Меню')
more_films = KeyboardButton('Еще!')
kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, )
kb_main_menu.add(menu, more_films)
