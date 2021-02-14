from config_handler import get_db_config
import sqlalchemy

db_conf = get_db_config()

PASSWD = db_conf['password']
HOST = db_conf['host']
PORT = db_conf['port']
USER = db_conf['user']

engine = sqlalchemy.create_engine(
    f'postgresql://{USER}:{PASSWD}@{HOST}/telega',
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    }
)
