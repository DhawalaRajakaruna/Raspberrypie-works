import requests
from time import sleep

# Correct the IP address format
raspberry_pi_ip = "http://192.168.241.161:5000"

# Send a request to turn the buzzer on
response_on = requests.get(f"{raspberry_pi_ip}/buzz/on")
print(response_on.text)

sleep(5)

# Send a request to turn the buzzer off
response_off = requests.get(f"{raspberry_pi_ip}/buzz/off")
print(response_off.text)
sleep(5)
