'''
Test optical encoder sensor

h/w connections:
Pi       Encoder
3.3V --- Vcc
GND  --- Gnd
3    --- A0

note:
D0 on encoder is not connected to Pi
'''

from time import sleep
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)           

INPUT_PIN = 3           
GPIO.setup(INPUT_PIN, GPIO.IN)           

while True: 
    if (GPIO.input(INPUT_PIN) == True):
            print('0')
    else:
            print('3.3')
    sleep(1)