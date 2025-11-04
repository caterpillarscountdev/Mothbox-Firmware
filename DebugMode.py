#!/usr/bin/python3

'''
This is a special script to debug mothboxes with which will
-Stop cron
-Stop the internet from going off
-Turning off the bright UV 
-stop the mothbox from shutting down
'''


import subprocess


#GPIO
import RPi.GPIO as GPIO
import time
import datetime
from datetime import datetime



now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Adjust the format as needed

subprocess.run(["/home/pi/Desktop/Mothbox/StopCron.py"])
subprocess.run(["/home/pi/Desktop/Mothbox/Attract_Off.py"])


subprocess.run(["/home/pi/Desktop/Mothbox/scripts/MothPower/stop_lowpower.sh"])
print("Wifi will remain on.")


with open("/home/pi/Desktop/Mothbox/controls.txt", "w") as file:
    for line in lines:
        if line.startswith("shutdown_enabled="):
            file.write("shutdown_enabled=False\n")  # Replace with False
            print("Shutdown off in controls.txt")
        else:
            file.write(line)  # Keep other lines unchanged
