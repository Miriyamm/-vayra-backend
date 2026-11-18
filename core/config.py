import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'vayra-super-secret-key')
    DEBUG = True