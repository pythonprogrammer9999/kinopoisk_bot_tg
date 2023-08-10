from aiogram import types
from aiogram.utils.markdown import hide_link


async def response_to_the_user(message: types.Message, items):
    trailers = f"<b>Трейлеры:</b>\n{items['videos']}" if items['videos'] else ''
    result = f"<b>{items['name']}</b>\n<b>Год: </b>{items['year']}\
<b> Страна: </b>{items['countries']}\n<b>Жанр: </b>{items['genres']}\n\
<b>Описание: </b>{items['description']}\n{hide_link(items['poster'])}\n{trailers}"
    await message.reply(result, parse_mode='HTML')
