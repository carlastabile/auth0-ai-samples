from configparser import ConfigParser


def load_config():
    config = ConfigParser()
    config.read(".config.local")

    return config

config = load_config()