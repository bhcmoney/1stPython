from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

switch = 18
switch2 = 15

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	print("switch: ", GPIO.input(switch))
	print("switch 2: ", GPIO.input(switch2))
	sleep(1)
