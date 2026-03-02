# 📺 SPI OLED Display – SSD1306 (Raspberry Pi Pico Series)

This folder contains an SPI-based OLED display example using the **SSD1306 controller**.

Supported boards:

- Raspberry Pi Pico H
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

---

# 📡 What is SPI?

SPI (Serial Peripheral Interface) is a high-speed serial communication protocol.

### 🔹 SPI Lines

- **MOSI** – Master Out Slave In  
- **MISO** – Master In Slave Out  
- **SCK** – Serial Clock  
- **CS** – Chip Select  

Additional control pins (for OLED):

- **DC** – Data/Command selection  
- **RST** – Reset  

---

# 🖥️ About SSD1306 OLED

The **SSD1306** is a popular OLED display controller.

### 🔹 Key Features
- 128x64 or 128x32 resolution
- Monochrome display
- Very low power consumption
- Supports **I2C and SPI communication**
- Works at 3.3V (perfect for Pico boards)

---

# 🔄 I2C vs SPI Mode (SSD1306)

| Feature | I2C Mode | SPI Mode |
|----------|-----------|-----------|
| Wires Used | 2 | 4+ |
| Speed | Moderate | Faster |
| Pin Usage | Low | Higher |
| Recommended For | Simple wiring | Faster display updates |

Your folder uses **SPI mode** for better speed and performance.

---

# 📂 Folder Structure

```
SPI/
 └── OLED Display/
       ├── main.py
       └── ssd1306.py
```

---

# 📄 File Description

### 🔹 ssd1306.py
- Driver file for SSD1306 display
- Supports both I2C and SPI versions
- Contains drawing functions:
  - pixel()
  - text()
  - fill()
  - show()
  - line()
  - rect()

This file can be reused for both I2C and SPI implementations.

---

### 🔹 main.py
- Initializes SPI interface
- Configures control pins (DC, RST, CS)
- Creates SSD1306 object
- Displays text or graphics on OLED

---

# ⚙️ SPI Configuration for Pico Boards

All boards (Pico H / W / 2W) support SPI identically.

### 🔹 Example Initialization

```python
from machine import Pin, SPI
import ssd1306

spi = SPI(
    0,
    baudrate=1000000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19)
)

dc = Pin(16)
rst = Pin(17)
cs = Pin(20)

oled = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

oled.fill(0)
oled.text("SPI OLED", 0, 0)
oled.show()
```

You can modify GPIO pins depending on your wiring.

---

# 🔌 Typical Wiring (SPI Mode)

| OLED Pin | Pico Pin |
|----------|----------|
| VCC | 3.3V |
| GND | GND |
| SCK | GPIO 18 |
| MOSI | GPIO 19 |
| DC | GPIO 16 |
| RST | GPIO 17 |
| CS | GPIO 20 |

---

# 🧠 Board Compatibility

| Feature | Pico H | Pico W | Pico 2 W |
|----------|----------|----------|------------|
| SPI Support | ✅ | ✅ | ✅ |
| Logic Level | 3.3V | 3.3V | 3.3V |
| Wireless Impact | ❌ | None on SPI | None on SPI |

Wireless stack (WiFi/BLE) does NOT affect SPI functionality.

---

# 🚀 Why Use SPI for OLED?

- Faster screen refresh
- Better for animations
- Better for graphics-heavy applications
- Less communication overhead

---

# 🛠 Switching to I2C Mode (Optional)

If your OLED module is I2C version, use:

```python
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
```

The same `ssd1306.py` driver supports both modes.

---

# 🎯 Purpose of This Module

- Learn SPI communication
- Interface graphical displays
- Display text, shapes, and animations
- Understand hardware abstraction via drivers

---
