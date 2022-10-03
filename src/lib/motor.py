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
    """A class that represents a DC Motor"""

    def __init__(self, pin1, pin2):
        """Function to initialize Motor object

        Args:
            pin1 (int): Pin number to which motor is attached
            pin2 (int): Pin number to which motor is attached
        """
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
