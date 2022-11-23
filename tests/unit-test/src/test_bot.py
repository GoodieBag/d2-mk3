from src.utils import setup_env
import src.constants as const

setup_env()

import RPi.GPIO as GPIO  # noqa: E402
from src.lib.bot import Bot  # noqa: E402


def test_init():
    """Test bot init"""
    bot = Bot()
    assert bot.motor_L.pin1 == const.MOTOR_L_PIN1
    assert bot.motor_L.pin2 == const.MOTOR_L_PIN2
    assert bot.motor_R.pin1 == const.MOTOR_R_PIN1
    assert bot.motor_R.pin2 == const.MOTOR_R_PIN2


def test_move_forwards():
    """Test bot move forwards"""
    bot = Bot()
    bot.move_forwards(auto_stop=False)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.HIGH
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.HIGH


def test_move_backwards():
    """Test bot move backwards"""
    bot = Bot()
    bot.move_backwards(auto_stop=False)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.HIGH
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.HIGH
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_turn_left():
    """Test bot turn left"""
    bot = Bot()
    bot.turn_left(auto_stop=False)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.HIGH
    assert GPIO.input(bot.motor_R.pin1) == GPIO.HIGH
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_turn_right():
    """Test bot turn right"""
    bot = Bot()
    bot.turn_right(auto_stop=False)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.HIGH
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.HIGH


def test_stop():
    """Test bot stop"""
    bot = Bot()
    bot.stop()
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_move_forwards_auto_stop():
    """Test bot move forwards auto stop"""
    bot = Bot()
    bot.move_forwards(auto_stop=True)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_move_backwards_auto_stop():
    """Test bot move backwards auto stop"""
    bot = Bot()
    bot.move_backwards(auto_stop=True)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_turn_left_auto_stop():
    """Test bot turn left auto stop"""
    bot = Bot()
    bot.turn_left(auto_stop=True)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW


def test_turn_right_auto_stop():
    """Test bot turn right auto stop"""
    bot = Bot()
    bot.turn_right(auto_stop=True)
    assert GPIO.input(bot.motor_L.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_L.pin2) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin1) == GPIO.LOW
    assert GPIO.input(bot.motor_R.pin2) == GPIO.LOW
