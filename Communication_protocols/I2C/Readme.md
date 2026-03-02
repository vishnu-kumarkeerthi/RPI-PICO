# 🔌 I2C Communication – Raspberry Pi Pico Series

This directory contains I2C (Inter-Integrated Circuit) communication examples for:

- Raspberry Pi Pico H  
- Raspberry Pi Pico W  
- Raspberry Pi Pico 2 W  

All examples are written in MicroPython and can be configured for any of the above boards.

---

# 📡 What is I2C?

I2C (Inter-Integrated Circuit) is a two-wire serial communication protocol used to connect multiple peripherals to a microcontroller.

### 🔹 I2C Lines
- **SDA** → Serial Data
- **SCL** → Serial Clock

### 🔹 Key Features
- Master–Slave architecture
- Multiple devices supported using unique addresses
- Only two wires required
- Low pin usage
- Suitable for short-distance communication

---

# 🎯 Typical Use Cases

- 16x2 LCD Displays (with I2C module)
- OLED Displays
- Temperature Sensors
- RTC (Real-Time Clock)
- EEPROM
- ADC/DAC Modules

---

# 📂 Folder Structure

```
I2C/
 ├── 16x2_LCD/
 │     ├── i2c_lcd.py
 │     ├── i2c_scan.py
 │     ├── lcd_api.py
 │     ├── main.py
 │     └── scrollingtext.py
```

---

# 📄 File Description

### 🔹 i2c_lcd.py
- Low-level driver for 16x2 LCD over I2C
- Sends commands and data to LCD
- Controls cursor, clear, and write operations

### 🔹 lcd_api.py
- Provides reusable LCD API functions
- Hardware-independent LCD interface layer
- Separates display logic from application logic

### 🔹 i2c_scan.py
- Scans I2C bus for connected devices
- Displays detected I2C addresses
- Useful for debugging wiring and connections

### 🔹 main.py
- Main execution file
- Initializes I2C bus
- Demonstrates LCD usage

### 🔹 scrollingtext.py
- Displays scrolling text on LCD
- Demonstrates dynamic text movement

---

# ⚙️ Configuring I2C for Pico H / Pico W / Pico 2 W

All boards operate at **3.3V logic level** and support **2 hardware I2C controllers**.

### 🔹 Example Initialization

```python
from machine import Pin, I2C

i2c = I2C(
    0,
    scl=Pin(1),
    sda=Pin(0),
    freq=400000
)
```

### 🔹 Changing Pins

You can change SDA and SCL pins based on wiring:

```python
i2c = I2C(1, scl=Pin(3), sda=Pin(2))
```

The Pico’s flexible pin mapping allows most GPIO pins to be used for I2C.

---

# 🧠 Board Compatibility Notes

| Feature | Pico H | Pico W | Pico 2 W |
|----------|----------|----------|------------|
| I2C Support | ✅ | ✅ | ✅ |
| Logic Level | 3.3V | 3.3V | 3.3V |
| I2C Controllers | 2 | 2 | 2 |

### Important:
- Pico H and Pico W have 3 external ADC pins (26–28)
- Pico 2 W has 4 external ADC pins (26–29)
- I2C configuration remains identical across boards
- Wireless features (WiFi/BLE) do NOT affect I2C functionality

---

# 🔍 Debugging I2C Connections

Before running display code:

1. Upload and run `i2c_scan.py`
2. Confirm device address appears (e.g., 0x27 or 0x3F for LCD)
3. Update address inside your driver if needed

Example scan output:
```
I2C devices found: [39]
```

---

# ⚡ Best Practices

- Use short wires for stable communication
- Use proper pull-up resistors (usually built into modules)
- Match I2C voltage levels (3.3V)
- Avoid long cables to prevent noise

---

# 🎯 Purpose of This I2C Module

- Understand two-wire serial communication
- Learn device addressing
- Interface displays and sensors
- Build foundation for embedded system communication

---

