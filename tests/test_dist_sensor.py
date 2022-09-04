"""
Test HC-SR04 distance sensor

h/w connections:
Pi       HC-SR04
5V   --- Vcc
GND  --- Gnd
15   --- Trig
11   --- Echo 1k-11-2k-GND (voltage divider)

note:
Pin 11 connected to Echo through voltage divider to get 3.3v from 5V echo
output
"""

import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 16
    PIN_ECHO = 18

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    while 1:
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        # print("Waiting for sensor to settle")
        time.sleep(2)

        # print("Calculating distance")
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print("Distance:", distance, "cm")

finally:
    GPIO.cleanup()
