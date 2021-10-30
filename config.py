from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
BOT_SALT = env.str("BOT_SALT")

USE_BOT_SALT = True
