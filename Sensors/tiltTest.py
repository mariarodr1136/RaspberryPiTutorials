import RPi.GPIO as GPIO
import time

TiltPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print(GPIO.input(TiltPin))
    time.sleep(0.5)
