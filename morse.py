import RPi.GPIO as GPIO
import time
import sys

MORSE = {
	' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

nPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(nPin, GPIO.OUT)
GPIO.setwarnings(False)
#GPIO.cleanup()

def punto():
	GPIO.output(nPin, 1)
	time.sleep(0.2)
	GPIO.output(nPin, 0)
	time.sleep(0.2)

def meno():
	GPIO.output(nPin, 1)
	time.sleep(0.5)
	GPIO.output(nPin, 0)
	time.sleep(0.2)

continua = 'y'
while(continua == 'y'):
	frase = input('Inserire la stringa da convertire: ')
	frase = frase.upper()
	print("\t\tASCII\t|\tMORSE")
	for c in frase:
		if c not in MORSE:
			sys.exit("Input non Valido !")
	for lettera in frase:
		print("Carattere:\t", lettera, "\t|\t", MORSE[lettera])
		for simbolo in MORSE[lettera]:
			if simbolo == '-':
				meno()
			elif simbolo == '.':
				punto()
			else:
				time.sleep(0.5)
		time.sleep(0.5)
        continua = input("Vuoi continuare ? y/n: ")
