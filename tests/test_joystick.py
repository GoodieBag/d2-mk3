import pygame
import sys

pygame.init()  # Loads pygame engine
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
                if j.get_axis(0) >= 0.5:
                    print ("right has been pressed")  # Right
                if j.get_axis(0) <= -1:
                    print ("left has been pressed")   # Left

                if j.get_axis(1) >= 0.5:
                    print ("Down has been pressed")  # Down
                if j.get_axis(1) <= -1:
                    print("Up has been pressed")
except pygame.error:
	print ("no joystick found.")
