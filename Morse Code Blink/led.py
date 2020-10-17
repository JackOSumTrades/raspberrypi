import RPi.GPIO as GPIO
import time

Led = 11
MORSE_CODE_DICT = {' ':' ', 'A':'.-', 'B':'-...', 
                            'C':'-.-.', 'D':'-..', 'E':'.', 
                                                'F':'..-.', 'G':'--.', 'H':'....', 
                                                                    'I':'..', 'J':'.---', 'K':'-.-', 
                                                                                        'L':'.-..', 'M':'--', 'N':'-.', 
                                                                                                            'O':'---', 'P':'.--.', 'Q':'--.-', 
                                                                                                                                'R':'.-.', 'S':'...', 'T':'-', 
                                                                                                                                                    'U':'..-', 'V':'...-', 'W':'.--', 
                                                                                                                                                                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                                                                                                                                                                                            '1':'.----', '2':'..---', '3':'...--', 
                                                                                                                                                                                                                '4':'....-', '5':'.....', '6':'-....', 
                                                                                                                                                                                                                                    '7':'--...', '8':'---..', '9':'----.', 
                                                                                                                                                                                                                                                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                                                                                                                                                                                                                                                                            '?':'..--..', '/':'-..-.', '-':'-....-', 
                                                                                                                                                                                                                                                                                                '(':'-.--.', ')':'-.--.-'} 
code = ''
DOT = 0.25
REST= 0.25
LINE=0.5
def enterCode():
    data = raw_input('Input text to translate in morse code ')
    code = data
    print('Outputting: ', code)
    return code
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Led, GPIO.OUT)
    GPIO.output(Led, GPIO.HIGH)
    
    code  = enterCode()
    return code
def code2morse(code):
    output = []
    for token in code.upper():
        print(token)
        output.append(MORSE_CODE_DICT.get(token))
    print('Morse: ', output)
    return output

def dot():
    print('DOT')
    GPIO.output(Led,GPIO.LOW)
    time.sleep(DOT)
    GPIO.output(Led,GPIO.HIGH)
    time.sleep(REST)
def space():
    print('SPACE')
    GPIO.output(Led, GPIO.HIGH)
    time.sleep(DOT)
def line():
    print('LINE')
    GPIO.output(Led, GPIO.LOW)
    time.sleep(LINE)
    GPIO.output(Led, GPIO.HIGH)
    time.sleep(REST)

def off():
    print('OFF')
    GPIO.output(Led, GPIO.HIGH)
    time.sleep(1)
def morse2signal(morse):
    for token in morse:
        if token == ' ':
            space()
            continue
        for sig in token:
            if sig == '.':
                dot()
            else:
                line()

def loop(code):
    while True:
        off()
        morse = code2morse(code)
        morse2signal(morse)        

def destroy():
    GPIO.output(Led, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    code = setup()
    try:
        loop(code)
    except KeyboardInterrupt:
        destroy()

