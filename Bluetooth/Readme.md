# 📡 Bluetooth (BLE) – Raspberry Pi Pico W / Pico 2 W

This folder contains Bluetooth Low Energy (BLE) examples for:

- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

⚠ Note: Standard Pico H does NOT support Bluetooth.

---

# 🧠 What is BLE?

Bluetooth Low Energy (BLE) is a low-power wireless communication protocol designed for:

- IoT devices
- Sensors
- Wearables
- Low-energy embedded systems

BLE works using two main roles:

| Role | Description |
|------|------------|
| **Peripheral** | Device that advertises data (e.g., sensor) |
| **Central** | Device that scans and connects (e.g., reader) |

---

# 📂 Folder Structure

```
Bluetooth/
 ├── ble_advertising.py
 ├── picow_ble_temp_sensor.py
 └── picow_ble_temp_reader.py
```

---

# 📄 File Description

---

## 🔹 ble_advertising.py

Helper module for:

- Creating BLE advertising payloads
- Encoding device name
- Encoding service UUID
- Decoding advertising packets

It allows the central device to detect specific services before connecting.

---

## 🔹 picow_ble_temp_sensor.py (Peripheral)

Acts as a BLE Temperature Sensor.

### Features:
- Uses Environmental Sensing Service (UUID 0x181A)
- Uses Temperature Characteristic (UUID 0x2A6E)
- Reads internal temperature sensor (ADC)
- Sends temperature every 10 seconds
- Supports:
  - Read
  - Notify
  - Indicate

### Data Format:
- Signed 16-bit integer
- Resolution: 0.01°C
- Example:
  - 2534 → 25.34°C

---

## 🔹 picow_ble_temp_reader.py (Central)

Acts as a BLE Client.

### Features:
- Scans for Environmental Sensing Service
- Connects automatically
- Discovers services and characteristics
- Reads temperature value
- Handles notifications
- Prints temperature to serial console
- Flashes onboard LED during read cycle

---

# 🔄 How It Works (Communication Flow)

```
Sensor (Peripheral)
     ↓ Advertising
Central Scans
     ↓
Connect
     ↓
Discover Service (0x181A)
     ↓
Discover Characteristic (0x2A6E)
     ↓
Read / Receive Notification
     ↓
Print Temperature
```

---

# ⚙️ Hardware Requirements

To test properly:

- 2 Pico W boards OR
- 2 Pico 2 W boards

Board 1:
→ Upload `picow_ble_temp_sensor.py`

Board 2:
→ Upload `picow_ble_temp_reader.py`

Make sure `ble_advertising.py` is uploaded to both boards.

---

# 🧪 How to Run

### 1️⃣ Upload files to Pico
- Use Thonny or mpremote
- Place files in root directory

### 2️⃣ Run Sensor Script
It will:
- Start advertising
- Print temperature every 10 seconds

### 3️⃣ Run Reader Script
It will:
- Scan for sensor
- Connect automatically
- Display temperature in shell

---

# 📊 Board Compatibility

| Feature | Pico W | Pico 2 W |
|----------|----------|------------|
| BLE Support | ✅ | ✅ |
| WiFi | ✅ | ✅ |
| ADC Temp Sensor | ✅ | ✅ |

Standard Pico H does NOT support BLE.

---

# 🔍 Internal Temperature Sensor

The sensor code reads:

```
ADC(4)
```

Temperature calculation:

```
27 - (V - 0.706) / 0.001721
```

This converts voltage to °C.

---

# 📡 Why Use BLE Instead of WiFi?

BLE is:
- Lower power
- Simpler pairing
- Ideal for short-range sensors
- Faster setup for local communication

WiFi is better for:
- Internet/cloud applications
- Long-range communication


---

# 🚀 Future Improvements

You can extend this example to:

- Add custom sensor services
- Send multiple characteristics
- Implement encryption
- Connect to smartphone BLE apps
- Combine BLE + WiFi hybrid applications

