import RPi.GPIO as GPIO
import time


# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set Rasp pins 11 and 12 as output and define PWM servo1 and servo2
GPIO.setup(11,GPIO.OUT)
neck=GPIO.PWM(11,50) # pin 11 for servo 1
GPIO.setup(12,GPIO.OUT)
head=GPIO.PWM(12,50) # pin 11 for servo 1

# Run PWM on both Servos, value of 0 (pulse off)
neck.start(0)
head.start(0)

# turn neck to 90
neck.ChangeDutyCycle(7)
time.sleep(0.5)
neck.ChangeDutyCycle(0)

time.sleep(2)

# turn head to 90
head.ChangeDutyCycle(7)
time.sleep(0.5)
head.ChangeDutyCycle(0)

time.sleep(2)

# reset servos
neck.ChangeDutyCycle(2)
neck.ChangeDutyCycle(0)

head.ChangeDutyCycle(2)
head.ChangeDutyCycle(0)

time.sleep(5)
neck.stop()
head.stop()
GPIO.cleanup()