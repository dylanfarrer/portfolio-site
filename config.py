import os

class Config:
    SECRET_KEY = os.urandom(50).hex()
