from sqlalchemy.sql.sqltypes import DateTime
from .models import Users, Films


class UserQuery:
    def create_user(session: 'Session', user_id: str, username: str):
        u = Users(user_id, username)
        session.add(u)

    def delete_user(session: 'Session', user_id: str):
        u = session.query(Users).filter(Users.user_id == user_id).one()
        session.delete(u)

    def get_user_by_user_id(session: 'Session', user_id: str):
        u = session.query(Users).filter(Users.user_id == user_id).one()
        return u


class FilmQuery:
    def create_film(
                    session: 'Session',
                    film_name: str,
                    date_created: DateTime,
                    user: Users):
        f = Films(film_name, date_created, user)
        session.add(f)

    def delete_film(
                    session: 'Session',
                    film_name: str,
                    user: Users):
        film = session.query(Films).filter(
                                          Films.film_name == film_name,
                                          Films.user.user_id == user).one()
        session.delete(film)

    def get_all_by_user(session: 'Session', user: Users):
        films = session.query(Films).filter(Films.user == user).all()
        return films
