import RPi.GPIO as GPIO
import time

PIR_PIN = 18
LED_PIN = 17
BUZZER_PIN = 27
ALERT_DURATION = 2.0 # seconds

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

GPIO.output(BUZZER_PIN, GPIO.LOW) # Ensure buzzer starts off
GPIO.output(LED_PIN, GPIO.LOW)    # Ensure LED starts off


def alarm_beeping():
    while GPIO.input(PIR_PIN):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)

def alert_on():
    """Turn on LED and buzzer for a short duration"""
    GPIO.output(LED_PIN, GPIO.HIGH)
    print(f'[{time.strftime('%H:%M:%S')}] Motion Detected! Alert On.')

def alert_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    print(f'[{time.strftime('%H:%M:%S')}] Alert Off.')



print('Task 7: PIR Motion Detection')
print('Waiting 10 seconds to callibrate')
for i in range(10, 0, -1):
    print(f'Calibrating... {i} seconds remaining')
    time.sleep(1)
print('PIR ready. Monitoring motion')

try:
    while True:
        if GPIO.input(PIR_PIN):
            alert_on()
            alarm_beeping()
            time.sleep(ALERT_DURATION) # Keep alert on for the duration
            alert_off()
            time.sleep(0.1) # Cooldown before checking for motion again
        time.sleep(0.1) # Check for motion every 100 ms

        # else:
        #     print('No Motion detected')

except KeyboardInterrupt:
    print('\nExiting...')

finally:
    alert_off() # Ensure alert is off before exiting
    GPIO.cleanup()