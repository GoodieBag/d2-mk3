import os
from src.utils import setup_env
import src.constants as const

setup_env()

import RPi.GPIO as GPIO  # noqa: E402
from src.lib.motor import Motor  # noqa: E402


def test_init():
    """Test motor init"""
    print(os.getenv("ENV"))
    motor = Motor(pin1=1, pin2=2)
    assert motor.pin1 == 1
    assert motor.pin2 == 2


def test_turn_clockwise():
    """Test motor turn clockwise"""
    motor = Motor(pin1=const.MOTOR_L_PIN1, pin2=const.MOTOR_L_PIN2)
    motor.turn_clockwise()
    assert GPIO.input(motor.pin1) == GPIO.LOW
    assert GPIO.input(motor.pin2) == GPIO.HIGH


def test_turn_anticlockwise():
    """Test motor turn anticlockwise"""
    motor = Motor(pin1=const.MOTOR_L_PIN1, pin2=const.MOTOR_L_PIN2)
    motor.turn_anticlockwise()
    assert GPIO.input(motor.pin1) == GPIO.HIGH
    assert GPIO.input(motor.pin2) == GPIO.LOW


def test_stop():
    """Test motor stop"""
    motor = Motor(pin1=const.MOTOR_L_PIN1, pin2=const.MOTOR_L_PIN2)
    motor.stop()
    assert GPIO.input(motor.pin1) == GPIO.LOW
    assert GPIO.input(motor.pin2) == GPIO.LOW
