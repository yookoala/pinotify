import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def switch(ev=None):
    print("switched")

GPIO.add_event_detect(17, GPIO.FALLING, callback=switch, bouncetime=300)

while True:
    time.sleep(1)
