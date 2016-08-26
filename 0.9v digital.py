import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    input_value = GPIO.input(18)
    print str(input_value)
    if input_value == 0:
        print "low"
    else:
        print "high"
    sleep(1)
