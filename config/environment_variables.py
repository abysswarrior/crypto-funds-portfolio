from decouple import config
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ON_HEROKU = config('ON_HEROKU', cast=bool)
CHROMEDRIVER_PATH = config('CHROMEDRIVER_PATH')
GOOGLE_CHROME_BIN = config('GOOGLE_CHROME_BIN', default=None)

RESTRICTED_AREA = config('RESTRICTED_AREA', default=False, cast=bool)

PROXY_HOST = config('PROXY_HOST', default=None)
PROXY_PORT = config('PROXY_PORT', default=None)