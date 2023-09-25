import os

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    PASSWORD = os.getenv('PASSWORD')
    FROM_EMAIL = os.getenv("FROM_EMAIL") 

# DATABASE_URI = config("DATABASE_URL")

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
