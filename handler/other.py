from aiogram import types, Dispatcher


async def echo_send(message: types.Message):
    await message.reply('Такой команды нет ')


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
