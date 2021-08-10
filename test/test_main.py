#from gpiozero import Servo
import pygame
import time
import sys
import pigpio

pi = pigpio.pi()

#servo1 = Servo(5)
#servo2 = Servo(6)

pygame.init()           # Loads pygame engine
pygame.joystick.init()  # main joystick device system

try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print ("Enabled joystick: {0}".format(j.get_name()))
    while 1:
        for e in pygame.event.get():
            #if e.type != pygame.QUIT: 
            #    print('%s: %s' % (pygame.event.event_name(e.type), e.dict))
            if e.type == pygame.JOYAXISMOTION:  # Joystick
                print(j.get_axis(0),j.get_axis(1))
                if j.get_axis(0) >= 0.5 :
                    print ("right has been pressed")  # Right
                    #servo2.min()
                    pi.set_servo_pulsewidth(6, 800)
                    #time.sleep(0.5)
                if j.get_axis(0) <= -1:
                    print ("left has been pressed")   # Left
                    #servo2.max()
                    pi.set_servo_pulsewidth(6, 1800)
                    #time.sleep(0.5)
                if j.get_axis(1) >= 0.5:
                    print ("Down has been pressed")  # Down
                    pi.set_servo_pulsewidth(5, 800)
                if j.get_axis(1) <= -1:
                    print("Up has been pressed")
                    pi.set_servo_pulsewidth(5, 1800)
            else:
                pass
                #pi.set_servo_pulsewidth(6, 1500)
                #pi.set_servo_pulsewidth(5, 1500)
except pygame.error:
	print ("no joystick found.")
