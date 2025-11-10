import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
motionPin = 12
GPIO.setup(motionPin, GPIO.IN)
time.sleep(15)
try:
    while True:
        if GPIO.input(motionPin):
            print("Motion Detected!")
            time.sleep(1)
        else:
            print("No Motion")
            time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped by User")
    GPIO.cleanup()
