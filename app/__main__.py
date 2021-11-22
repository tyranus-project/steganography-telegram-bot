from loguru import logger

from app.main import main


try:
    main()
except (KeyboardInterrupt, SystemExit):
    logger.info("Bot stopped")
