import RPi.GPIO as GPIO
import time 

LED_PIN = 17
BLINK_DELAY = 0.5

#--------------------SETUP----------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

print('Task 01 started. LED blinking. Press Ctrl+C to stop.')

#-----------Main Loop------------
while True:
	GPIO.output(LED_PIN, GPIO.HIGH)
	print('LED ON')
	time.sleep(BLINK_DELAY)

	GPIO.output(LED_PIN, GPIO.LOW)
	print('LED OFF')
	time.sleep(BLINK_DELAY)
