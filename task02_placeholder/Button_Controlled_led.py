import  RPi.GPIO as GPIO
import time 

LED_PIN = 17
BUTTON_PIN = 22


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# PUD up means that it will read the pin high normally and low when pressed

print('Task 02 started. Press the button to toggle LED. Ctr+C to stop')

led_state = False

def button_pressed(channel):
    global led_state
    led_state = not led_state
    GPIO.output(LED_PIN, led_state)
    state_str = 'ON' if led_state else 'OFF'
    print(f'Button pressed. LED state is now {state_str}')

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, 
                    callback=button_pressed, 
                    bouncetime=200)

while True:
    time.sleep(0.1)



