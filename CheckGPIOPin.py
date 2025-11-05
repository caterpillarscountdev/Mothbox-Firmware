#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Set pin numbering mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Define GPIO pin for checking
off_pin = 16
debug_pin = 12

# Function to check for connection to ground
def pin_connected_to_ground(pin):
  for i in range(4):
      # Retry loop for caught errors only
      try:
          GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

          # Read the pin value
          pin_value = GPIO.input(pin)

          # If pin value is LOW (0), then it's connected to ground
          return pin_value == 0
      except GPIO.lgpio.error as e:
        time.sleep(0.5)
      finally:
        GPIO.cleanup()

def mode():
  mode= "ACTIVE" # possible modes are OFF or DEBUG or ACTIVE
  if pin_connected_to_ground(debug_pin):
    mode= "DEBUG"

  if pin_connected_to_ground(off_pin):
    mode = "OFF" #this check comes second as the OFF state should override the DEBUG state in case both are attached
  return mode

if __name__ == "__main__":
    print(mode())

    # Clean up GPIO on exit
    GPIO.cleanup()
