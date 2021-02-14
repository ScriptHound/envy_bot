import logging
import types
import asyncio
import re

from sqlalchemy.orm import session, sessionmaker
from aiogram import Bot, Dispatcher, executor, types

from config_handler import get_bot_token
from db_config import engine
from main_app.queries import UserQuery

API_TOKEN = get_bot_token()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
Session = sessionmaker(bind=engine)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    logging.info(message.text)
    await message.reply("Привет, я Энви :)")


@dp.message_handler(commands=['Посмотреть'])
async def echo(message: types.Message):
    film_name = ""
    logging.info(message['from']['id'])
    try:
        logging.info(message.text)
        film_name = re.search(r"^.*\s(.*)", str(message.text)).group(1)
    except AttributeError:
        await message.answer('Ты что-то не то написал...')
    await message.answer(f'Хорошо, я записала: {film_name}')


@dp.message_handler(commands=['create_user'])
async def create_user(message: types.Message):
    conn = engine.connect()
    session = Session(bind=conn)

    from_id = message['from']['id']
    username = message['from']['username']
    try:
        UserQuery.create_user(session, from_id, username)
        session.commit()
    except Exception:
        session.rollback()
        raise RuntimeError('DB Transaction failed')
    finally:
        session.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
