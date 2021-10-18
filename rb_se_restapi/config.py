import os

class DB:
    DATABASE_URL = os.getenv('POSTGRES_DB_URL')
    DATABASE_NAME = os.getenv('POSTGRES_DB_NAME')
    DATABASE_USER = os.getenv('POSTGRES_USER')
    DATABASE_PASSWORD = os.getenv('postgres_password')