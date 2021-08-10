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

# Create a function to run when the input is high
def inputLow(channel):
    print('0')

GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback=inputLow, bouncetime=200) # Wait for the input to go low, run the function when it does

while True:
    print('3.3');
    sleep(1);           