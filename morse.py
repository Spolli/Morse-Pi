import RPi.GPIO as GPIO
import time
import sys

#A dictionary to converto from human alphabet to morse alphabet
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

#set pin to output
nPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(nPin, GPIO.OUT)
GPIO.setwarnings(False)


def dot():
	GPIO.output(nPin, 1)
	time.sleep(0.2)
	GPIO.output(nPin, 0)
	time.sleep(0.2)

def dash():
	GPIO.output(nPin, 1)
	time.sleep(0.5)
	GPIO.output(nPin, 0)
	time.sleep(0.2)

continue = 'y'
while(continue == 'y'):
	frase = input('Insert the string to convert: ')
	frase = frase.upper()
	print("\t\tASCII\t|\tMORSE")
	for c in frase:
		if c not in MORSE:
			sys.exit("Invalid input!")
	for lettera in frase:
		print("Carattere:\t", lettera, "\t|\t", MORSE[lettera])		#convert the string to morse code
		for simbolo in MORSE[lettera]:
			if simbolo == '-':
				dash()
			elif simbolo == '.':
				dot()
			else:
				time.sleep(0.5)
		time.sleep(0.5)
        continue = input("Do you want to continue? y/n: ")
