import time
import board
import adafruit_dht

# Set the sensor type and the GPIO pin (GPIO16 corresponds to board.D16)
dhtDevice = adafruit_dht.DHT11(board.D16)  # Change to D16 for GPIO16

while True:
    try:
        # Read the temperature and humidity from the sensor
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        # Print the readings
        print(f"Temp: {temperature:.1f}C  Humidity: {humidity}%")

    except RuntimeError as error:
        # Catch errors like read failures and try again
        print(error.args[0])

    time.sleep(2)  # Delay before the next reading
