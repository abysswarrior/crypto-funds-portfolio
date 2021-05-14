from decouple import config

ON_HEROKU = config('ON_HEROKU', cast=bool)
CHROMEDRIVER_PATH = config('CHROMEDRIVER_PATH')
RESTRICTED_AREA = config('RESTRICTED_AREA', default=False, cast=bool)

PROXY_HOST = config('PROXY_HOST', default=None)
PROXY_PORT = config('PROXY_PORT', default=None)