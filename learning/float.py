from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

switch = 17

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	print("switch: ", GPIO.input(switch))
	sleep(1)
