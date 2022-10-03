import os


def setup_env():
    # replace RPi.GPIO with fake GPIO if environment is DEV
    if os.getenv("ENV") != "PROD":
        print("Running in dev mode")

        # Replace libraries by fake ones
        import sys
        import fake_rpi

        sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
        sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
        # fake_rpi.toggle_print(False)
