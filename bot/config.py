import uuid

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

SKIP_UPDATES = env.bool("SKIP_UPDATES", default=False)
THROTTLING_RATE_LIMIT = env.float("THROTTLING_RATE_LIMIT", default=0.1)

DATA_DIR = env.str("DATA_DIR", default="/data")

SESSION_SALT = uuid.uuid4().hex
