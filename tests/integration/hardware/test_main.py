import pygame
import time
import pigpio

from test_dc_motor import Motor

pi = pigpio.pi()

pygame.init()  # Loads pygame engine
pygame.joystick.init()  # main joystick device system

MAX_RIGHT = 800
MAX_LEFT = 2200
CENTER = 1500
value = CENTER
value_y = CENTER

try:
    j = pygame.joystick.Joystick(0)  # create a joystick instance
    j.init()  # init instance
    print("Enabled joystick: {0}".format(j.get_name()))
    left_motor = Motor(38, 22)
    right_motor = Motor(11, 12)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.JOYAXISMOTION:  # Joystick
                print(j.get_axis(0), j.get_axis(1))
                if j.get_axis(0) >= 0.5:
                    print("right has been pressed")  # Right
                    if value >= MAX_RIGHT:
                        value -= 10
                    else:
                        value = MAX_RIGHT
                    pi.set_servo_pulsewidth(6, value)
                if j.get_axis(0) <= -1:
                    print("left has been pressed")  # Left
                    if value <= MAX_LEFT:
                        value += 20
                    else:
                        value = MAX_LEFT
                    pi.set_servo_pulsewidth(6, value)
                if j.get_axis(1) >= 0.5:
                    print("Down has been pressed")  # Down
                    if value_y >= MAX_RIGHT:
                        value_y -= 50
                    else:
                        value_y = MAX_RIGHT
                    pi.set_servo_pulsewidth(5, value_y)
                if j.get_axis(1) <= -1:
                    print("Up has been pressed")
                    if value_y <= MAX_LEFT:
                        value_y += 50
                    else:
                        value_y = MAX_LEFT
                    pi.set_servo_pulsewidth(5, value_y)
                # motor
                if j.get_axis(2) >= 0.5:
                    print("right has been pressed")  # Right
                    left_motor.turn_clockwise()
                    right_motor.turn_anticlockwise()
                    time.sleep(0.2)
                    left_motor.stop()
                    right_motor.stop()
                if j.get_axis(2) <= -1:
                    print("left has been pressed")  # Left
                    left_motor.turn_anticlockwise()
                    right_motor.turn_clockwise()
                    time.sleep(0.2)
                    left_motor.stop()
                    right_motor.stop()
                if j.get_axis(3) >= 0.5:
                    print("Down has been pressed")  # Down
                    left_motor.turn_anticlockwise()
                    right_motor.turn_anticlockwise()
                    time.sleep(0.2)
                    left_motor.stop()
                    right_motor.stop()
                if j.get_axis(3) <= -1:
                    print("Up has been pressed")
                    left_motor.turn_clockwise()
                    right_motor.turn_clockwise()
                    time.sleep(0.2)
                    left_motor.stop()
                    right_motor.stop()
            else:
                pass
except pygame.error:
    print("no joystick found.")
