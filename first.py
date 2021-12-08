import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

def center_lock(angle):
    servo1.ChangeDutyCycle(7)
    servo2.ChangeDutyCycle(7)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    
def move_right(angle):
    servo1.ChangeDutyCycle(angle-0.1)
    time.sleep(0.1)
    servo1.ChangeDutyCycle(0)
    
def move_left(angle):
    servo1.ChangeDutyCycle(angle+0.1)
    time.sleep(0.1)
    servo1.ChangeDutyCycle(0)

def move_up(angle):
    servo2.ChangeDutyCycle(angle+0.1)
    time.sleep(0.1)
    servo2.ChangeDutyCycle(0)
    
def move_down():
    servo2.ChangeDutyCycle(angle-0.1)
    time.sleep(0.1)
    servo2.ChangeDutyCycle(0)
    
    
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(12)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)

servo1.stop()
servo2.stop()
GPIO.cleanup()

