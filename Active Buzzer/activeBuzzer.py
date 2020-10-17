import RPi.GPIO as GPIO
import time

out_pin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.output(out_pin, GPIO.LOW)

def loop():
    while True:
        GPIO.output(out_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(out_pin, GPIO.LOW)
        time.sleep(0.5)

def destroy():
    GPIO.output(out_pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
