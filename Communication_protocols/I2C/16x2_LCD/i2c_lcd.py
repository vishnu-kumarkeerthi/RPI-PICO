
# I2C LCD driver for HD44780-compatible 16x2 LCD using PCF8574 I2C backpack.
# Works with any RP2040 board (Pico / Pico W / Pico 2 W) when an I2C object is provided.


from lcd_api import LcdApi
from machine import I2C
import time


class I2cLcd(LcdApi):
    # PCF8574 pin definitions
    MASK_RS = 0x01
    MASK_RW = 0x02
    MASK_E = 0x04
    MASK_BACKLIGHT = 0x08

    def __init__(self, i2c, i2c_addr, num_lines=2, num_columns=16):
        """Initialize the LCD"""
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.backlight = self.MASK_BACKLIGHT

        # LCD Initialization sequence
        time.sleep_ms(20)
        self.hal_write_init_nibble(0x03)
        time.sleep_ms(5)
        self.hal_write_init_nibble(0x03)
        time.sleep_us(200)
        self.hal_write_init_nibble(0x03)
        time.sleep_us(200)
        self.hal_write_init_nibble(0x02)

        # Set 4-bit mode, 2-line display, 5x8 font
        self.write_command(0x28)
        self.write_command(0x0C)
        self.write_command(0x06)
        self.clear()

    def hal_write_init_nibble(self, nibble):
        """Send 4 bits to the LCD during initialization"""
        data = (nibble << 4) | self.backlight
        self.i2c.writeto(self.i2c_addr, bytes([data | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([data]))

    def write_command(self, cmd):
        """Send command to LCD"""
        self.hal_write(cmd, 0)

    def write_data(self, data):
        """Send data to LCD"""
        self.hal_write(data, self.MASK_RS)

    def hal_write(self, data, rs_mask):
        """Send high and low nibble data to LCD"""
        high_nibble = (data & 0xF0) | self.backlight | rs_mask
        low_nibble = ((data << 4) & 0xF0) | self.backlight | rs_mask

        # Send high nibble
        self.i2c.writeto(self.i2c_addr, bytes([high_nibble | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([high_nibble]))

        # Send low nibble
        self.i2c.writeto(self.i2c_addr, bytes([low_nibble | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([low_nibble]))

    def move_to(self, col, row):
        """Move the cursor to the specified position"""
        row_offsets = [0x00, 0x40]

        row = max(0, min(1, row))
        col = max(0, min(15, col))

        pos = 0x80 | (col + row_offsets[row])
        self.write_command(pos)

    def clear(self):
        """Clear the LCD display"""
        self.write_command(0x01)
        time.sleep_ms(2)

    def putstr(self, string):
        """Display a string on the LCD"""
        for char in string:
            self.write_data(ord(char))
