import yaml


def get_db_config():
    with open('config.yml') as conf:
        return yaml.load(conf.read(), Loader=yaml.Loader)['database']


def get_bot_token():
    with open('config.yml') as conf:
        return yaml.load(conf.read(), Loader=yaml.Loader)['bot_token']['token']