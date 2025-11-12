import RPi.GPIO as GPIO
import time
buzzPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin,GPIO.OUT)
buzz=GPIO.PWM(buzzPin,400)
buzz.start(50)
try:
    while True:
        for i in range(150,2000):
            buzz.ChangeFrequency(i)
            time.sleep(0.0001)
        for i in range(2000,150,-1):
            buzz.ChangeFrequency(i)
            time.sleep(0.0001)
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program stopped by User")
