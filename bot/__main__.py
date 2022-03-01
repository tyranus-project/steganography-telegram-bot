from loguru import logger

from bot.main import main


try:
    main()
except (KeyboardInterrupt, SystemExit):
    logger.info("Steganography bot stopped.")
