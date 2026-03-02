# Example application to display characters on a 16x2 I2C LCD using I2cLcd driver.
# Works on Raspberry Pi Pico / Pico W / Pico 2 W with any valid I2C pin mapping.
"""

Folder structure 
project/
│── lcd_api.py        # Base LCD API
│── i2c_lcd.py        # I2C LCD driver (PCF8574)
│── main.py       # This file (application)

LCD sequential character display using I2C (PCF8574 backpack)

Compatible boards:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W
- Rhodium 

Only change the I2C CONFIG section if needed.
"""

from machine import I2C, Pin
from time import sleep
from i2c_lcd import I2cLcd

# -------------------------------------------------
# I2C CONFIGURATION 
# -------------------------------------------------
I2C_BUS = 0            # 0 or 1
I2C_SDA_PIN = 0        # GPIO number
I2C_SCL_PIN = 1        # GPIO number
I2C_FREQ = 100_000     # 100 kHz

I2C_ADDR = 0x27        # LCD I2C address (change if needed)
LCD_ROWS = 2
LCD_COLS = 16
# -------------------------------------------------

# Initialize I2C
i2c = I2C(
    I2C_BUS,
    sda=Pin(I2C_SDA_PIN),
    scl=Pin(I2C_SCL_PIN),
    freq=I2C_FREQ
)

# Initialize LCD
lcd = I2cLcd(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Startup message
lcd.clear()
lcd.putstr("Starting...")
sleep(2)
lcd.clear()

# Data to send
data = "abcdefghijklmnopqrstuvwxyz"

print("[INFO] Sending data to LCD...")

# Send characters one by one
for char in data:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(f"Sending: {char}")
    print("Sent:", char)
    sleep(1)

lcd.clear()
lcd.putstr("Done!")
print("[INFO] Data transmission complete.")


