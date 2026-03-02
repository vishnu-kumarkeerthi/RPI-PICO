
# Base LCD API for HD44780-compatible character displays.
# Provides common LCD commands; hardware-specific drivers must subclass this.


import time


class LcdApi:
    # LCD Commands
    LCD_CLR = 0x01
    LCD_HOME = 0x02
    LCD_ENTRY_MODE = 0x04
    LCD_ON_OFF = 0x08
    LCD_SHIFT = 0x10
    LCD_FUNCTION = 0x20
    LCD_CGRAM = 0x40
    LCD_DDRAM = 0x80

    # Entry Mode parameters
    LCD_ENTRY_INC = 0x02
    LCD_ENTRY_SHIFT = 0x01

    # On/Off control parameters
    LCD_ON = 0x04
    LCD_CURSOR_ON = 0x02
    LCD_BLINK_ON = 0x01

    def __init__(self):
        self.num_lines = 2
        self.num_columns = 16
        self.cursor_x = 0
        self.cursor_y = 0

    def clear(self):
        """ Clear display """
        self.write_command(self.LCD_CLR)
        time.sleep_ms(2)

    def home(self):
        """ Return cursor to home position """
        self.write_command(self.LCD_HOME)
        time.sleep_ms(2)

    def write_command(self, cmd):
        """ Placeholder for sending command to LCD """
        pass

    def write_data(self, data):
        """ Placeholder for sending data to LCD """
        pass

    def move_to(self, row, col):
        """ Move cursor to specified row and column """
        if row >= self.num_lines or col >= self.num_columns:
            return

        self.cursor_x = col
        self.cursor_y = row
        addr = col + 0x40 * row
        self.write_command(self.LCD_DDRAM | addr)

    def putstr(self, string):
        """ Display a string on the LCD """
        for char in string:
            self.write_data(ord(char))

    def backlight_on(self):
        """ Turn backlight on """
        pass

    def backlight_off(self):
        """ Turn backlight off """
        pass