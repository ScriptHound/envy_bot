import logging
import types
import asyncio
import re
import datetime

import psycopg2
from sqlalchemy.orm import sessionmaker
from aiogram import Bot, Dispatcher, executor, types

from config_handler import get_bot_token
from db_config import engine
from main_app.queries import FilmQuery, UserQuery

API_TOKEN = get_bot_token()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
Session = sessionmaker(bind=engine)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    logging.info(message.text)
    await message.reply("Привет, я Энви :)")


@dp.message_handler(commands=['create_film'])
async def create_film(message: types.Message):
    conn = engine.connect()
    session = Session(bind=conn)
    from_id = str(message['from']['id'])
    curtime = datetime.datetime.now()

    try:
        # user = UserQuery.get_user_by_user_id(session, from_id)
        film_name = re.search(r"^.*\s(.*)", str(message.text)).group(1)
        FilmQuery.create_film(session, film_name, curtime, from_id)

        session.commit()
        await message.answer(f'Я записала, {film_name}!')
    except Exception:
        session.rollback()
        await message.answer('Ой, что-то пошло не так(')
        raise RuntimeError('Film creation failure')
    finally:
        session.close()


@dp.message_handler(commands=['create_user'])
async def create_user(message: types.Message):
    conn = engine.connect()
    session = Session(bind=conn)

    from_id = message['from']['id']
    username = message['from']['username']
    try:
        UserQuery.create_user(session, from_id, username)
        session.commit()
    except psycopg2.errors.UniqueViolation:
        session.rollback()
        await message.answer(f'Юзер {username} уже есть))0')
    finally:
        session.close()


@dp.message_handler(commands=['delete_user'])
async def delete_user(message: types.Message):
    conn = engine.connect()
    session = Session(bind=conn)

    user_id = '289436398'
    try:
        UserQuery.delete_user(session, user_id)
        session.commit()
    except Exception:
        session.rollback()
        raise RuntimeError("User deleting failed")
    finally:
        session.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
