"""
Scrolling text demo for a 16x2 I2C LCD (PCF8574)

Compatible boards:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W
- Any Pico-reference board

Only modify the I2C CONFIG section if needed.
"""

from machine import I2C, Pin
from time import sleep
from i2c_lcd import I2cLcd

# -------------------------------------------------
# I2C CONFIGURATION 
# -------------------------------------------------
I2C_BUS = 1            # 0 or 1
I2C_SDA_PIN = 2        # GPIO number
I2C_SCL_PIN = 3        # GPIO number
I2C_FREQ = 400_000     # 100_000 or 400_000

I2C_ADDR = 0x27        # LCD I2C address
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
lcd.clear()

# Message to scroll
message = "  Hello Hi catch me if you can     "
window_size = LCD_COLS  # Automatically matches LCD width

# Scroll the text
while True:
    for i in range(len(message) - window_size + 1):
        lcd.move_to(0, 0)
        lcd.putstr(message[i:i + window_size])
        sleep(0.5)
