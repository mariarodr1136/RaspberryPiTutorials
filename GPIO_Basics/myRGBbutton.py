import RPi.GPIO as GPIO
from time import sleep
dt=.1

rPin=37
gPin=35
bPin=33

rBut=11
gBut=13
bBut=15

rButState=1
rButStateOld=1

gButState=1
gButStateOld=1

bButState=1
bButStateOld=1

rLEDstate=0
gLEDstate=0
bLEDstate=0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.setup(rBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		rButState=GPIO.input(rBut)
		gButState=GPIO.input(gBut)
		bButState=GPIO.input(bBut)
		print('Button States',rButState,gButState,bButState)
		if rButState==1 and rButStateOld==0:
			print('Red Channel Registered')
			rLEDstate= not rLEDstate
			GPIO.output(rPin,rLEDstate)
		if gButState==1 and gButStateOld==0:
			print('Green Channel Registered')
			gLEDstate= not gLEDstate
			GPIO.output(gPin,gLEDstate)
		if bButState==1 and bButStateOld==0:
			print('Blue Channel Registered')
			bLEDstate= not bLEDstate
			GPIO.output(bPin,bLEDstate)
		rButStateOld=rButState
		gButStateOld=gButState
		bButStateOld=bButState
		sleep(dt)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO GOOD TO GO')
