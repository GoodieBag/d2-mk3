"""Class for motor control

Bot uses two 90 rpm DC motors

Hardware connections:
Pi       H-Bridge motor driver
5    --- motorA1
6    --- motorA2
13   --- motorB1
26   --- motorB2
"""

import RPi.GPIO as GPIO


class Motor:
    """
    A class used to represent a DC motor
    Attributes
    ----------
    pin1 : int
        valid RPi GPIO pin number (DEFAULT value - 5)
    pin2 : int
        valid RPi GPIO pin number (DEFAULT value - 6)
    Methods
    -------
    turn_clockwise()
        rotates the motor in clockwise direction
    turn_anticlockwise()
        rotates the motor in anticlockwise direction
    stop()
        stops the motor rotation
    """

    def __init__(self, pin1, pin2):
        """Function to init pins used by the motor as output"""
        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setmode(GPIO.BCM)  # use BCM numbering for GPIO
        GPIO.setwarnings(False)  # Ignore GPIO warnings

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

    def turn_clockwise(self):
        """Function to move motor in clockwise direction"""
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    def turn_anticlockwise(self):
        """Function to move motor in anticlockwise direction"""
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def stop(self):
        """Function to stop motor rotation"""
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.cleanup()
