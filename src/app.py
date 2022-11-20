from src.utils.logger import setup_logger


def init_loggers():
    setup_logger("hardware", file_name="hardware.log")
    setup_logger("software", file_name="software.log")


if __name__ == "__main__":
    init_loggers()
