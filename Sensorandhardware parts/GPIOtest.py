import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the LED
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
print("everything is set")

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second
        print("ON")
        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second
        print("Off")
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()