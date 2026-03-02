This repository contains practical examples and implementations for Raspberry Pi Pico H, Pico W, and Pico 2 W. It covers GPIO, Communication Protocols, Bluetooth, WiFi, and Peripheral Interfaces.
# 🍓 RPI-PICO Projects Repository

This repository contains practical examples and implementations for:

- **Raspberry Pi Pico H**
- **Raspberry Pi Pico W**
- **Raspberry Pi Pico 2 W**

It covers:

- GPIO
- Communication Protocols (I2C, SPI, UART, USB)
- Bluetooth (BLE)
- WiFi
- Peripheral Interfaces

---

#  What is the Raspberry Pi Pico?

The Raspberry Pi Pico is a **low-cost, high-performance microcontroller board**  
(It is NOT a single-board computer like Raspberry Pi 4/5.)

It is designed for:

- Embedded systems
- IoT projects
- Robotics
- Hardware control
- Education & experimentation

---

# 🔹 Primary Use Cases

### ✅ Embedded Control
- Motor control
- Sensor reading
- Automation systems

### ✅ IoT Devices
- WiFi / BLE based data transmission
- Cloud-connected sensors
- Smart home systems

### ✅ Peripheral Interface Bridge
- USB ↔ I2C
- USB ↔ SPI
- USB ↔ UART

---

# ⚙️ Technical Specifications Comparison

> Note: Pico H refers to the standard Pico (RP2040) with pre-soldered headers.  
> Silicon is identical to standard Pico.

| Feature | Pico H | Pico W | Pico 2 W |
|----------|----------|----------|------------|
| **MCU** | RP2040 (Dual-core Cortex-M0+) | RP2040 + CYW43439 | RP2350 (Dual-core Cortex-M33 / RISC-V) |
| **Max CPU Frequency** | 133 MHz | 133 MHz | 150 MHz |
| **Wireless** | ❌ None | ✅ WiFi 4 (2.4GHz) + BLE 5.2 | ✅ WiFi 4 (2.4GHz) + BLE 5.2 |
| **Flash** | 2 MB | 2 MB | 4 MB |
| **SRAM** | 264 KB | 264 KB | 520 KB |
| **GPIO Pins** | 26 Multi-function | 26 Multi-function | 26 Multi-function |
| **ADC Channels** | 3 External + Temp | 3 External + Temp | 4 External + Temp |
| **I2C Controllers** | 2 | 2 | 2 |
| **SPI Controllers** | 2 | 2 | 2 |
| **UART Controllers** | 2 | 2 | 2 |
| **PWM** | 16 slices (32 outputs) | 16 slices | 16 slices |
| **USB** | USB 1.1 (Device/Host) | USB 1.1 | USB 1.1 |
| **Logic Level** | 3.3V | 3.3V | 3.3V |

---

# 🔌 Peripheral Details

### 🔹 I2C (Inter-Integrated Circuit)
- 2-wire communication (SDA, SCL)
- Used for: LCDs, OLEDs, sensors
- Supports multiple devices via addressing
- Best for low-speed peripherals

### 🔹 SPI (Serial Peripheral Interface)
- Faster than I2C
- Used for: Displays, ADCs, DACs, SD cards
- Requires MOSI, MISO, SCK, CS
- Suitable for high-speed communication

### 🔹 UART (Universal Asynchronous Receiver Transmitter)
- TX / RX communication
- Used for GPS, GSM, serial debugging
- Simple and widely supported

### 🔹 USB
- Used for programming and debugging
- Direct PC communication
- Power + Data interface

---

# 📌 When to Consider Each Board

## 🔹 Raspberry Pi Pico H (Standard)

Use Pico H when:

- You do NOT need wireless connectivity
- You want the most cost-effective solution
- You need maximum GPIO availability
- Wired communication is sufficient

---

## 🔹 Raspberry Pi Pico W

Use Pico W when:

- You need WiFi connectivity (IoT)
- You need Bluetooth (BLE)
- You want cost-effective wireless solution
- You want same RP2040 performance with wireless support

---

## 🔹 Raspberry Pi Pico 2 W

Use Pico 2 W when:

- You need higher performance (150 MHz)
- You need more memory (520KB SRAM)
- You require advanced real-time applications
- You need better security (Arm TrustZone)
- You want future-proof wireless systems

---

# 🆚 Added Advantages

| Comparison | Advantage |
|------------|------------|
| Pico 2 W vs Pico W | ~20% faster CPU (150 MHz) |
| Pico 2 W vs Pico W | Double SRAM (520 KB) |
| Pico 2 W vs Pico W | More advanced Cortex-M33 core |
| Pico W vs Pico H | Adds WiFi & BLE |
| Pico H vs Pico W | No wireless stack overhead |

---

# 📂 Folder Structure Overview

```
Blink/
Bluetooth/
Communication_protocols/
GPIO/
Wifi/
demo/
README.md
```

---

# 📡 Communication Protocols (Inside Repository)

Inside `Communication_protocols/`, examples are provided for:

- I2C (LCD, OLED)
- SPI (Displays)
- UART (Serial communication)
- USB communication

Each folder contains working examples and test programs.

---

# ⚙️ Configuration Support

This repository supports:

- Pico H
- Pico W
- Pico 2 W

You can configure and modify code based on your hardware requirement.

Wireless examples are included for both Pico W and Pico 2 W.


