from sqlalchemy.sql.sqltypes import DateTime
from .models import Users, Films


class UserQuery:
    def create_user(session: 'Session', user_id: str, username: str):
        u = Users(user_id, username)
        session.add(u)


class FilmQuery:
    def create_film(
                    session: 'Session',
                    film_name: str,
                    date_created: DateTime,
                    user: Users):
        f = Films(film_name, date_created, user)
        session.add(f)
