import requests

# Replace with your Raspberry Pi's IP address
raspberry_pi_ip = "http://192.168.241.161:5000"


# The word you want to send
message = "Hello Dhawala"  # Change to any word/message you want

# Sending GET request to display the message on the Raspberry Pi LCD
response = requests.get(f"{raspberry_pi_ip}/display/{message}")

# Print the server's response
print(response.text)
