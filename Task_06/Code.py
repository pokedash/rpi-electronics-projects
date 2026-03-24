import RPi.GPIO as GPIO
import time

TRIG_PIN = 23
ECHO_PIN = 24
SPEED_OF_SOUND_CM_PPER_S = 34300 # ~ 343 m/s

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(TRIG_PIN, GPIO.LOW) # Ensure Trig starts low
time.sleep(0.5)                 # Wait for sensor to settle

def measure_distance_cm():
    """Send a 10 micorsecond trigger pulse and time the echo return"""
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001) # 10 microseconds
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Wait for echo to go high and record the start time
    pulse_start = time.time()
    timeout = pulse_start + 0.1 # 100 ms timeout
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            return None # Timeout waiting for echo

    # Wait for echo to go low and record the end time
    pulse_end = time.time()
    timeout = pulse_end + 0.1 # 100 ms timeout
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            return None # Echo never returned

    pulse_duration = pulse_end - pulse_start
    distance_cm = (pulse_duration * SPEED_OF_SOUND_CM_PPER_S) / 2
    return distance_cm

print('Task 6: Ultrasonic Distance Measurement')

try:
    while True:
        distance = measure_distance_cm()
        if distance is not None:
            print(f'Distance: {distance} cm')
        else:
            print('Measurement failed - check wiring')
        time.sleep(1) # Wait before next measurement
except KeyboardInterrupt:
    print('Exiting...')
finally:
    GPIO.cleanup()