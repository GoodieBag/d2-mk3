from utils import setup_env


def bot_init():
    """Function to initialize bot"""
    print("Initializing bot")
    setup_env()

    from lib.bot import Bot

    return Bot()


if __name__ == "__main__":
    bot = bot_init()
    # bot.move_forwards()
    # bot.move_backwards()
    # bot.turn_left()
    # bot.turn_right()
