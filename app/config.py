from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

SKIP_UPDATES = env.bool("SKIP_UPDATES", default=False)
THROTTLING_RATE_LIMIT = env.float("THROTTLING_RATE_LIMIT", default=0.1)
