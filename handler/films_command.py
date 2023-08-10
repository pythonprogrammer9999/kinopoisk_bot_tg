from aiogram import types
from handler.send_request import response_to_the_user
from kinopoisk.create_kinopoisk import kp
from kinopoisk.create_kinopoisk import headers
import requests
import random


async def get_random_movie(message: types.Message):
    item = kp.random()
    try:
        poster = item.poster.url
    except:
        poster = ''
    try:
        videos = ''.join(trailer.url for trailer in item.videos.trailers),
    except:
        videos = ''
    results = {
        'name': item.name,
        'year': item.year,
        'countries': ', '.join([country.name for country in item.countries]),
        'genres': ', '.join([country.name for country in item.genres]),
        'description': item.description,
        'poster': poster,
        'videos': ''.join(videos)
    }
    await response_to_the_user(message, results)


async def get_random_movie_by_genre(message: types.Message, genres):
    year_range = "2020-2023"
    response = requests.get(
        'https://api.kinopoisk.dev/v1.3/movie',
        params={
            "genres.name": genres,
            "year": year_range,
            "rating.kp": "5-10",
        },
        headers=headers
    )
    movies = response.json()
    total_pages = movies["total"] // movies["limit"] + (1 if movies["total"] % movies["limit"] > 0 else 0)
    random_page = random.randint(1, total_pages)
    response = requests.get(
        'https://api.kinopoisk.dev/v1.3/movie',
        params={
            "genres.name": genres,
            "page": random_page,
            "year": year_range,

        },
        headers=headers
    )
    movies = response.json()['docs'][0]['id']
    response = requests.get(
        f'https://api.kinopoisk.dev/v1/movie/{movies}',
        headers=headers
    )
    movies = response.json()
    try:
        poster = movies['poster']['url'],
    except:
        poster = ''
    try:
        videos = (', '.join([trailer['url'] for trailer in movies['videos']['trailers'][:3]])),

    except:
        videos = ''
    results = {
        'name': movies['name'],
        'year': movies['year'],
        'countries': ', '.join([country['name'] for country in movies['countries']]),
        'genres': ', '.join([country['name'] for country in movies['genres']]),
        'description': movies['description'],
        'poster': poster,
        'videos': ''.join(videos)
    }

    await response_to_the_user(message, results)


async def get_best_movies_by_genres(message: types.Message, genres, page=1):
    limit = 3
    response = requests.get(
        'https://api.kinopoisk.dev/v1.3/movie',
        params={
            "genres.name": genres,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = []
    my_try = response.json()['docs']
    for x in my_try:
        movies.append(x['id'])

    response = []
    new_movies = []
    for i in range(len(movies)):
        response.append(requests.get(
            f'https://api.kinopoisk.dev/v1/movie/{movies[i]}',
            headers=headers
        ))
        new_movies.append(response[i].json())
        try:
            poster = new_movies[i]['poster']['url'],
        except:
            poster = ''
        try:
            videos = ', '.join([trailer['url'] for trailer in new_movies[i]['videos']['trailers'][:3]])
        except:
            videos = ''
        results = {
            'name': new_movies[i]['name'],
            'year': new_movies[i]['year'],
            'countries': ', '.join([country['name'] for country in new_movies[i]['countries']]),
            'genres': ', '.join([country['name'] for country in new_movies[i]['genres']]),
            'description': new_movies[i]['description'],
            'poster': poster,
            'videos': videos,
        }
        await response_to_the_user(message, results)
