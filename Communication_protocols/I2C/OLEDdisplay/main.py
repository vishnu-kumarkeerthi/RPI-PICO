"""
SSD1306 OLED demo using I2C (MicroPython)

Compatible boards:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

"""

from machine import Pin, I2C
import ssd1306
import time

# -------------------------------------------------
# I2C CONFIGURATION (GENERALIZED)
# -------------------------------------------------
I2C_BUS = 0            # 0 or 1
I2C_SDA_PIN = 4        # GPIO number
I2C_SCL_PIN = 5        # GPIO number
I2C_FREQ = 400_000     # 100_000 or 400_000

OLED_ADDR = 0x3C       # Common SSD1306 I2C address
OLED_WIDTH = 128
OLED_HEIGHT = 64
# -------------------------------------------------

# Initialize I2C
i2c = I2C(
    I2C_BUS,
    sda=Pin(I2C_SDA_PIN),
    scl=Pin(I2C_SCL_PIN),
    freq=I2C_FREQ
)

# Initialize OLED
oled = ssd1306.SSD1306_I2C(
    OLED_WIDTH,
    OLED_HEIGHT,
    i2c,
    addr=OLED_ADDR
)

# Clear display
oled.fill(0)

# Display text
oled.text("OLED TEST", 0, 0)
oled.text("Raspberry Pi", 0, 16)
oled.text("Pico Family", 0, 32)

oled.show()

# Keep running
while True:
    time.sleep(1)
