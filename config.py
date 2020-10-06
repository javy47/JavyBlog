import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-you-think-you-can-guess-this=?'