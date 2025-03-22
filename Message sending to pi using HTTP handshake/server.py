from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep
import time
import board
#import adafruit_dht
# server.py (on Raspberry Pi)
from flask import Flask
from gpiozero import OutputDevice
from threading import Thread

app = Flask(__name__)

# Define GPIO to LCD mapping using OutputDevice
LCD_RS = OutputDevice(25)  # Pin 25 for RS
LCD_E = OutputDevice(24)  # Pin 24 for Enable
LCD_D4 = OutputDevice(23)  # Pin 23 for D4
LCD_D5 = OutputDevice(18)  # Pin 18 for D5
LCD_D6 = OutputDevice(15)  # Pin 15 for D6
LCD_D7 = OutputDevice(14)  # Pin 14 for D7

Buzzer = PWMOutputDevice(12)

# Define LCD parameters
LCD_WIDTH = 16  # Maximum characters per line
LCD_CHR = True  # Mode - Sending data
LCD_CMD = False  # Mode - Sending command
LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005



# Frequency values for different notes (in Hz)
C4 = 261  # C note
D4 = 294  # D note
E4 = 329  # E note
F4 = 349  # F note
G4 = 392  # G note
A4 = 440  # A note
B4 = 466  # B note

def play_tone(frequency, duration):
    """Generate a tone at a given frequency for a given duration."""
    Buzzer.frequency = frequency
    Buzzer.value = 0.5  # Set the buzzer volume (50% duty cycle)
    time.sleep(duration)
    Buzzer.value = 0  # Turn off the buzzer

def play_melody():
    """Play a simple melody."""
    # Play a series of notes (melody)
    play_tone(C4, 0.5)
    play_tone(D4, 0.5)
    play_tone(E4, 0.5)
    play_tone(F4, 0.5)
    play_tone(G4, 0.5)
    play_tone(A4, 0.5)
    play_tone(B4, 0.5)
    play_tone(C4, 1.0)  # End with a long C note

def lcd_init():
    """Initialize the LCD display."""
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Initialize
    lcd_byte(0x28, LCD_CMD)  # 2 line 5x7 matrix
    lcd_byte(0x0C, LCD_CMD)  # Turn cursor off
    lcd_byte(0x06, LCD_CMD)  # Shift cursor right
    lcd_byte(0x01, LCD_CMD)  # Clear display
    sleep(E_DELAY)

def lcd_byte(bits, mode):
    """Send byte to data pins."""
    # Send mode (True for data, False for command)
    LCD_RS.value = mode

    # High bits
    LCD_D4.off()
    LCD_D5.off()
    LCD_D6.off()
    LCD_D7.off()
    
    if bits & 0x10:
        LCD_D4.on()
    if bits & 0x20:
        LCD_D5.on()
    if bits & 0x40:
        LCD_D6.on()
    if bits & 0x80:
        LCD_D7.on()

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    LCD_D4.off()
    LCD_D5.off()
    LCD_D6.off()
    LCD_D7.off()
    
    if bits & 0x01:
        LCD_D4.on()
    if bits & 0x02:
        LCD_D5.on()
    if bits & 0x04:
        LCD_D6.on()
    if bits & 0x08:
        LCD_D7.on()

    # Toggle 'Enable' pin
    lcd_toggle_enable()

def lcd_toggle_enable():
    """Toggle enable pin."""
    sleep(E_DELAY)
    LCD_E.on()
    sleep(E_PULSE)
    LCD_E.off()
    sleep(E_DELAY)

def lcd_string(message, line):
    """Send string to display."""
    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

@app.route('/display/<message>', methods=['GET'])
def display_message(message):
    # Clear the display and show the message
    play_melody()
    lcd_string(f"{message}", LCD_LINE_1)
    sleep(5)
    lcd_string(" ", LCD_LINE_1)
    return f"Message displayed: {message}"


# Main program loop
if __name__ == '__main__':
    #dhtDevice = adafruit_dht.DHT11(board.D16)
    lcd_init()
    app.run(host='0.0.0.0', port=5000)