import RPi.GPIO as GPIO
import time

#-- Config--
LED_PIN= 17		# BCM GPIO pin number
BLINK_DELAY = 0.5 	# Seconds between on/off

#-- setup--
GPIO.setmode(GPIO.BCM)	#Use BCM pin numbering
GPIO.setwarnings(False)	#Suppress duplicate warnings
GPIO.setup(LED_PIN, GPIO.OUT)	#Set GIPO17 as an output pin

#--Main Loop--
while True:
	GPIO.output(LED_PIN, GPIO.HIGH)		#Turn on LED
	print('LED on')
	time.sleep(BLINK_DELAY)

	GPIO.output(LED_PIN, GPIO.LOW)		#Turn off LED
	print('LED OFF')
	time.sleep(BLINK_DELAY)
