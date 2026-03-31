import RPi.GPIO as GPIO
import time
from enum import Enum, auto

#------- GPIO pins ----------------
RED_PIN = 17
YELLOW_PIN = 25
GREEN_PIN = 22
BUTTON_PIN = 27


# -------------------- States ---------
class State(Enum):
    GREEN = auto()
    YELLOW = auto()
    RED = auto()
    PED_REQUEST = auto()

# -------------------- Timing (seconds) -----
TIMING = {
    State.GREEN: 10,
    State.YELLOW: 3,
    State.RED: 10,
    State.PED_REQUEST: 5
}


# -------------------- LED config per state ---------
LED_CONFIG = {
    State.GREEN:        (False, False, True),   # Red, Yellow, Green
    State.YELLOW:       (False, True, False),
    State.RED:          (True, False, False),
    State.PED_REQUEST:  (True, False, False) # Red + Yellow for pedestrian
}

# -------------------- GPIO setup -------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in (RED_PIN, YELLOW_PIN, GREEN_PIN):
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button with pull-up resistor

pedestrian_req = False

def button_callback(channel):
    global pedestrian_req
    pedestrian_req = True
    print('Pedestrian crossing requested')

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, 
                        callback=button_callback, bouncetime=500)

def set_leds(red, yellow, green):
    GPIO.output(RED_PIN, GPIO.HIGH if red else GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.HIGH if yellow else GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH if green else GPIO.LOW)

def run_state(state):
    red, yellow, green = LED_CONFIG[state]
    set_leds(red, yellow, green)
    duration = TIMING[state]
    print(f'{time.strftime("%H:%M:%S")} - State: {state.name}, for {duration}s')
    time.sleep(TIMING[state])

def next_state(current):
    if current == State.GREEN:
        return State.YELLOW
    elif current == State.YELLOW:
        return State.RED
    elif current == State.RED:
        return State.GREEN
    elif current == State.PED_REQUEST:
        return State.GREEN

print('Task 9: Traffic Light with Pedestrian Button Ctr+C to stop')

current_state = State.RED # start at Red

try:
    while True:
        if current_state == State.YELLOW and pedestrian_req:
            current_state = State.PED_REQUEST
        run_state(current_state)
        current_state = next_state(current_state)

except KeyboardInterrupt:
    print('\nExiting...')

finally:
    set_leds(False, False, False)
    GPIO.cleanup()