from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# switch = 18
switch = 15

# GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	# print("switch: ", GPIO.input(switch))
	print("switch: ", GPIO.input(switch))
	sleep(1)
