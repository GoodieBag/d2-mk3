import os


def bot_init():
    """Function to initialize bot"""
    print("Initializing bot")

    # replace RPi.GPIO with fake GPIO if environment is DEV
    if os.getenv("ENV") == "DEV":
        print("Running in dev mode")

        # Replace libraries by fake ones
        import sys
        import fake_rpi

        sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
        sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO

    from lib.bot import Bot

    return Bot()


if __name__ == "__main__":
    bot = bot_init()
