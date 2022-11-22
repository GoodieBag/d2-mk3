import logging
from utils.environment import setup_env
from utils.logger import setup_logger


def init_loggers():
    """Function to initialize logger"""
    setup_logger("hardware", file_name="hardware.log")
    setup_logger("software", file_name="software.log")


def bot_init():
    """Function to initialize bot"""
    logger = logging.getLogger("hardware")
    logger.info("Initializing bot")
    setup_env()

    from lib.bot import Bot

    return Bot()


if __name__ == "__main__":
    init_loggers()
    bot = bot_init()
    # bot.move_forwards()
    # bot.move_backwards()
    # bot.turn_left()
    # bot.turn_right()
