import os



#load config from env

DB_URI = os.getenv("DB_URI")



#config

ACCESS_TOKEN_EXPIRY = 5 * 60
REFRESH_TOKEN_EXPIRY = 60 * 60 * 24
