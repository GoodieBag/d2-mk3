import logging
import os

logs_path = "../logs/"
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

default_log_format = (
    "%(asctime)s:%(filename)s:%(levelname)s:" + "%(message)s:%(lineno)d"
)

logging.basicConfig(
    filename=logs_path + "root.log",
    level=logging.WARNING,
    format=default_log_format,
)


def get_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger


def get_file_handler(name, level, format_str=default_log_format):
    file_handler = logging.FileHandler(logs_path + name)
    file_handler.setLevel(level)
    formatter = logging.Formatter(format_str)
    file_handler.setFormatter(formatter)
    return file_handler


def get_stream_handler(level, format_str=default_log_format):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    formatter = logging.Formatter(format_str)
    stream_handler.setFormatter(formatter)
    return stream_handler


def setup_logger(
    module_name,
    logger_level=logging.DEBUG,
    file_handler_level=logging.WARNING,
    stream_handler_level=logging.DEBUG,
    propagate=False,
):
    logger = get_logger(module_name, logger_level)
    logger.addHandler(get_file_handler(module_name, file_handler_level))
    logger.addHandler(get_stream_handler(level=stream_handler_level))
    logger.propagate = propagate
    return logger
