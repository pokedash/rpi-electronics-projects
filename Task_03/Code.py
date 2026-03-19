import RPi.GPIO as GPIO
import time

LED_PIN = 17
FREQUENCY = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)


# Create a pwm object on LED_PIN at 100hz
pwm = GPIO.PWM(LED_PIN, FREQUENCY)
pwm.start(0)	#start pwm with 0 duty cycle (OFF)

print('Task 03: PWM dimmer. LED iading in and out. Ctrl+C to stop')

while True:
	# Fade IN --> Increasing brightness from 0% to 100%

	print('Increasing Brightness of LED')
	for duty in range(0,101):
		pwm.ChangeDutyCycle(duty)
		time.sleep(0.02)	#wait 20ms between each step

	# Fade OUT --> decrese brightness from 100% to 0%
	print('Dimming LED')
	for duty in range (100, -1, -1):
		pwm.ChangeDutyCycle(duty)
		time.sleep(0.02)
