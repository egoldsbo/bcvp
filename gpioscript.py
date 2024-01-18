import RPi.GPIO as GPIO
import time

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BOARD) # or GPIO.BOARD

# Replace 17 with the GPIO pin number you want to use
pin = 6 

# Set up the GPIO pin as an output
GPIO.setup(pin, GPIO.OUT)

# Set the GPIO to HIGH
GPIO.output(pin, GPIO.HIGH)
time.sleep(10)  # Wait for 5 seconds

# Set the GPIO to LOW
GPIO.output(pin, GPIO.LOW)

# Clean up the GPIO settings
GPIO.cleanup()
