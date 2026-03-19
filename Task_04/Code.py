import RPi.GPIO as GPIO
import time


RED_PIN = 22
GREEN_PIN = 27
BLUE_PIN = 17
FREQ = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in (RED_PIN, GREEN_PIN, BLUE_PIN):
    GPIO.setup(pin, GPIO.OUT)

# Create pwm objects for each color pin
r_pwm = GPIO.PWM(RED_PIN, FREQ)
g_pwm = GPIO.PWM(GREEN_PIN, FREQ)
b_pwm = GPIO.PWM(BLUE_PIN, FREQ)

r_pwm.start(0)
g_pwm.start(0)
b_pwm.start(0)

def set_color(r, g, b):
    # set RGB LED colour. Values 0 - 255 mapped to 0-100% duty cycle
    r_pwm.ChangeDutyCycle(r/255*100)
    g_pwm.ChangeDutyCycle(g/255*100)
    b_pwm.ChangeDutyCycle(b/255*100)

# list of rainbow colors
rainbow = [
    (255, 0, 0),    # RED
    (255, 165, 0),  # ORANGE
    (255, 255, 0),  # YELLOW
    (0, 255, 0),    # GREEN
    (0, 0, 255),    # BLUE
    (75, 0, 130),   # INDIGO
    (148, 0, 211)   # VIOLET
]

print('Task 04: RGB LED. Cycle through rainbow colors. Ctrl+C to stop')

while True:
    for r,g,b in rainbow:
        set_color(r, g, b)
        colour_name = f'RGB ({r}, {g}, {b})'
        print(f'setting colour to {colour_name}')
        time.sleep(5)