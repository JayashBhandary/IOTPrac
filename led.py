import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

for i in range(1,10000):
    GPIO.output(17, True)
    time.sleep(0.08)
    GPIO.output(17, False)
    time.sleep(0.08)
    GPIO.output(18, False)
    time.sleep(0.08)
    GPIO.output(22, True)
    time.sleep(0.08)
    GPIO.output(22, False)
    time.sleep(0.08)