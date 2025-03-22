# server.py (on Raspberry Pi)
from flask import Flask
from gpiozero import OutputDevice

app = Flask(__name__)

# Set up the buzzer
Buzzer = OutputDevice(17)  # Connect the buzzer to GPIO 17

@app.route('/buzz/on', methods=['GET'])
def buzz_on():
    Buzzer.on()
    return "Buzzer turned on!"

@app.route('/buzz/off', methods=['GET'])
def buzz_off():
    Buzzer.off()
    return "Buzzer turned off!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Flask app runs on port 5000
