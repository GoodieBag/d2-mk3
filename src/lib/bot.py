"""Class to control the locomotion of the bot"""

from src.lib.motor import Motor


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

    def __init__(self, motor_L=None, motor_R=None):
        """Function to initialize two motor as output"""
        if motor_L is None:
            self.motor_L = Motor(pin1=5, pin2=6)
        else:
            self.motor_L = motor_L

        if motor_R is None:
            self.motor_R = Motor(pin1=13, pin2=26)
        else:
            self.motor_L = motor_L

    def move_forwards(self):
        """Function to move bot in forward direction"""
        self.motor_L.turn_clockwise()
        self.motor_R.turn_clockwise()

    def move_backwards(self):
        """Function to move bot in backward direction"""
        self.motor_L.turn_anticlockwise()
        self.motor_R.turn_anticlockwise()

    def turn_left(self):
        """Function to turn bot in left direction"""
        self.motor_L.turn_anticlockwise()
        self.motor_R.turn_clockwise()

    def turn_right(self):
        """Function to turn bot in right direction"""
        self.motor_L.turn_clockwise()
        self.motor_R.turn_anticlockwise()
