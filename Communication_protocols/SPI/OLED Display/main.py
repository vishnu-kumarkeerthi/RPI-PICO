"""
SSD1306 OLED SPI demo – display words sequentially

Compatible boards:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

Uses SPI1. Change only the CONFIG section if needed.
"""

from machine import Pin, SPI
import ssd1306
import time

# -------------------------------------------------
# SPI CONFIGURATION (GENERALIZED)
# -------------------------------------------------
SPI_BUS = 1

SPI_SCK_PIN  = 10    # GP10
SPI_MOSI_PIN = 11    # GP11
SPI_CS_PIN   = 9     # GP9
SPI_DC_PIN   = 8     # GP8
SPI_RES_PIN  = 12    # GP12

SPI_BAUDRATE = 10_000_000  # 10 MHz

OLED_WIDTH  = 128
OLED_HEIGHT = 64
# -------------------------------------------------

# Initialize SPI
spi = SPI(
    SPI_BUS,
    baudrate=SPI_BAUDRATE,
    polarity=0,
    phase=0,
    sck=Pin(SPI_SCK_PIN),
    mosi=Pin(SPI_MOSI_PIN)
)

# Control pins
dc  = Pin(SPI_DC_PIN, Pin.OUT)
cs  = Pin(SPI_CS_PIN, Pin.OUT)
res = Pin(SPI_RES_PIN, Pin.OUT)

# Initialize OLED (SPI)
oled = ssd1306.SSD1306_SPI(
    OLED_WIDTH,
    OLED_HEIGHT,
    spi,
    dc,
    res,
    cs
)

# List of words to display
words = [
    "HELLO",
    "SPI OLED",
    "RASPBERRY",
    "PI PICO",
    "PICO W",
    "PICO 2 W",
    "MICROPYTHON",
    "DONE"
]

# Display words one after another
while True:
    for word in words:
        oled.fill(0)                  # Clear display
        oled.text(word, 0, 0)         # Display word
        oled.show()
        time.sleep(1.5)               # Delay between words

