import RPi.GPIO as GPIO
import time
import threading

def listen_for_exit_command():
    global exit_command_received
    while True:
        if input("Type 'exit' to stop the program: ").lower() == 'exit':
            exit_command_received = True
            break

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM) # or GPIO.BOARD

# Replace 17 with the GPIO pin number you want to use
pin = 6 

# Set up the GPIO pin as an output
GPIO.setup(pin, GPIO.OUT)

# Flag to determine if exit command is received
exit_command_received = False

# Start a thread to listen for the exit command
exit_thread = threading.Thread(target=listen_for_exit_command)
exit_thread.start()

try:
    while not exit_command_received:
        # Set the GPIO to HIGH
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(10)  # Wait for 10 seconds

        # Set the GPIO to LOW
        GPIO.output(pin, GPIO.LOW)
        time.sleep(10)  # Wait for 10 seconds
finally:
    # Clean up the GPIO settings on exit
    GPIO.cleanup()
    exit_thread.join()  # Ensure the exit command thread is terminated properly
