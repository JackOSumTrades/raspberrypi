import RPi.GPIO as GPIO
import time
import getch

NOTES_4 = {'c':261.626, 'd':293.665, 'e':329.628, 'f':349.228, 'g':391.995, 'a':440,'b':493.883}

OUT = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OUT, GPIO.OUT)
    GPIO.output(OUT, GPIO.HIGH)

def loop():
    pwm = GPIO.PWM(OUT, 1000)
    pwm.start(50)
    while True:
        token = getch.getch()
        if token == 'z' or token == 'Z':
            break
        try:
            freq = NOTES_4.get(token)
            pwm.ChangeFrequency(freq)
        except:
            pass
        print(token)
def destroy():
    GPIO.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
