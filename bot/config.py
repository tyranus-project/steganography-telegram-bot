import uuid

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

SKIP_UPDATES = env.bool("SKIP_UPDATES", default=True)

DATA_DIR = env.str("DATA_DIR", default="/data")

SESSION_SALT = uuid.uuid4().hex
