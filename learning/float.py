from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN)

while True:
      print GPIO.input(11) 
      time.sleep(.5)