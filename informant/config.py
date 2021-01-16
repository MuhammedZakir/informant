"""
informant/config.py

This module contains helpers to manage arguments, options and configuration
settings provided to Informant.
"""

class Singleton():
    """ A Singleton class to be used as a base """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InformantConfig(metaclass=Singleton):
    """ Class to store global Informant arguments/options and configuration """

    def __init__(self):
        self.argv = {}
        self.config = {}
        self.colors = {
                'RED': '\033[0;31m',
                'YELLOW': '\033[1;33m',
                'CLEAR': '\033[0m',
                'BOLD': '\033[1m'
        }

    def set_argv(args):
        self.argv = args

    def get_argv():
        return self.argv

    def set_config(config):
        self.config = config

    def get_config():
        return self.config