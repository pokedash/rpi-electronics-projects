# Task 02 - Button Controlled LED

## Objective
- learn what pull up/down resistors are
- learn GPIO.add.event_detect
-

## Components Used
- Button
- LED
- jumper wires
- Breadboard
- resistor (220 ohms)

## Gpio wiring

#### LED
LED same as task_01

#### Button
Anode(+) --> GPIO 27
Cathode(-) --> GND (same as led pin 6)

## What I struggled with 
The line GPIO.add.event_detect was not working due to a library issue. I was able to resolve the issue by updating the library and could torubleshoot it with the help of AI

## What I learned 
- GPIO.add.event_detect
- pull upp/down resistors
- How to troubleshoot with AI