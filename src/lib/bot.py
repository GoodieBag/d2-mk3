"""Class to control the locomotion of the bot"""

import time
import constants as const
from lib.motor import Motor


class Bot:
    """
    A class used to represent a bot
    Attributes
    ----------
    motor_L : Motor
        motor object for left motor
    motor_R : Motor
        motor object for right motor
    Methods
    -------
    move_forwards()
        moves the bot in forward direction
    move_backwards()
        moves the bot in backward direction
    turn_left()
        turns the bot in left direction
    turn_right()
        turns the bot in right direction
    """

    def __init__(self):
        """Function to initialize two motor as output"""
        self.motor_L = Motor(pin1=const.MOTOR_L_PIN1, pin2=const.MOTOR_L_PIN2)
        self.motor_R = Motor(pin1=const.MOTOR_R_PIN1, pin2=const.MOTOR_R_PIN2)

    def move_forwards(self, auto_stop=True):
        """Function to move bot in forward direction"""
        self.motor_L.turn_clockwise()
        self.motor_R.turn_clockwise()
        time.sleep(const.BOT_MOTOR_ON_TIME_IN_SECONDS)

        if auto_stop:
            self.stop()

    def move_backwards(self, auto_stop=True):
        """Function to move bot in backward direction"""
        self.motor_L.turn_anticlockwise()
        self.motor_R.turn_anticlockwise()
        time.sleep(const.BOT_MOTOR_ON_TIME_IN_SECONDS)

        if auto_stop:
            self.stop()

    def turn_left(self, auto_stop=True):
        """Function to turn bot in left direction"""
        self.motor_L.turn_clockwise()
        self.motor_R.turn_anticlockwise()
        time.sleep(const.BOT_MOTOR_ON_TIME_IN_SECONDS)

        if auto_stop:
            self.stop()

    def turn_right(self, auto_stop=True):
        """Function to turn bot in right direction"""
        self.motor_L.turn_anticlockwise()
        self.motor_R.turn_clockwise()
        time.sleep(const.BOT_MOTOR_ON_TIME_IN_SECONDS)

        if auto_stop:
            self.stop()

    def stop(self):
        """Function to stop bot"""
        self.motor_L.stop()
        self.motor_R.stop()
