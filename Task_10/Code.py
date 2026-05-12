import RPi.GPIO as GPIO
import time
from numpy import random

#------- GPIO pins ----------------
RED_LED = 17
RED_BUTTON = 27

GREEN_LED = 22
GREEN_BUTTON = 18

YELLOW_LED = 25
YELLOW_BUTTON = 24

# -------------------- GPIO setup -------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for BUTTON in RED_BUTTON, GREEN_BUTTON, YELLOW_BUTTON:
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button

for LED in RED_LED, GREEN_LED, YELLOW_LED:
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW) # Ensure LEDs starts off

# -------------- Function ----------------------

def RandomButton():
    Color = random.choice(['RED', 'GREEN', 'YELLOW'])

    if Color == 'RED':
        return 27, 17

    elif Color == 'GREEN':
        return 18, 22
    
    elif Color == 'YELLOW':
        return 24, 25


def StartTest(BUTTON, LED):
    button_pressed = False
    GPIO.output(LED, GPIO.HIGH)
    start_time = time.time()
    while time.time() - start_time < 5:
        val = GPIO.input(BUTTON)
        if val == 0:
            end_time = time.time()
            GPIO.output(LED, GPIO.LOW)
            print('Button pressed')
            print(f'You took {end_time - start_time} seconds')
            button_pressed = True
            time.sleep(0.1)
            break

        else:
            time.sleep(0.01)


    if not button_pressed:
        print('You didn\'t press the button in time!')
        GPIO.output(LED, GPIO.LOW)




print('Task 10: Reaction Time Test')

try:
    while True:
        # calculating random time between 1 and 5 seconds
        premature_click = False
        BUTTON, LED = RandomButton()
        delay = random.random() * 4 + 1 
        start_time = time.time()

        print('Get ready...')


        while time.time() - start_time < delay:
            if GPIO.input(RED_BUTTON) == 0 or GPIO.input(YELLOW_BUTTON) == 0 or GPIO.input(GREEN_BUTTON) == 0:
                premature_click = True
                break

            
        if premature_click:
            print('You clicked prematurely, dont do it again')
            time.sleep(0.5)

        else:
            StartTest(BUTTON, LED)

        



except KeyboardInterrupt:
    print('\nExiting...')

finally:
    GPIO.cleanup()