import RPi.GPIO as GPIO
import time
buzzPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin,GPIO.OUT)
try:
    while True:
        GPIO.output(buzzPin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(buzzPin,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program stopped by User")
