import RPi.GPIO as GPIO
import ADC0834
import time
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
buttonPin=21
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  

try:
    while True:
        analogValX=ADC0834.getResult(0)
        time.sleep(0.1)
        analogValY=ADC0834.getResult(1)
        buttonState=GPIO.input(buttonPin)
        print('X-Value: ', analogValX, 'Y-Value: ', analogValY, 'Button State: ', buttonState)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned up and Exiting")
