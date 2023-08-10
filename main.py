from aiogram.utils import executor
from create_bot import dp
from handler import client, films_command, other


async def on_startup(_):
    print('Бот вышел в онлайн')


client.register_handler_client(dp)
other.register_handler_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
