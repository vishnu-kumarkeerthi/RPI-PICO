# 🔌 USB (CDC) Command & Streaming Interface  
Raspberry Pi Pico Series

This module implements a **Generic USB (CDC) Command & Streaming Interface** using MicroPython.

Supported boards:

- Raspberry Pi Pico (RP2040)
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W
- RP2040-based reference boards

---

# 📡 What is USB (CDC)?

USB CDC (Communication Device Class) allows the Pico to behave like a **virtual serial port** when connected to a computer.

When you connect the Pico via USB:
- It appears as a COM port
- You can send commands from a PC
- You can receive structured data
- No external hardware is required

---

# 🎯 When to Use USB Instead of UART / BLE / WiFi

### ✅ Use USB When:
- Direct PC communication is needed
- Debugging embedded systems
- Sending commands from Python terminal
- Logging real-time data
- No wireless communication required
- Reliable wired connection preferred

---

# 🆚 Advantages of USB Over Other Protocols

| Feature | USB | UART | BLE | WiFi |
|----------|------|------|------|------|
| External Wiring | ❌ None | ✅ Required | ❌ | ❌ |
| Speed | High | Medium | Medium | High |
| Range | Short (Cable) | Short | Short | Long |
| Power + Data | ✅ | ❌ | ❌ | ❌ |
| Setup Complexity | Low | Low | Medium | High |
| Internet Access | ❌ | ❌ | ❌ | ✅ |

### 🔹 Why USB is Powerful:
- Stable wired connection
- No pairing or networking setup
- Immediate command-response interface
- Ideal for development & testing

---

# 📂 File Overview

```
USB/
 └── main.py   (Generic USB Command Interface)
```

---

# 🧠 Code Explanation

This script implements:

- USB command interface
- LED control
- Sensor reading
- Periodic data streaming
- Non-blocking input handling

---

# ⚙️ Hardware Configuration

### 🔹 LED Initialization

```python
led = machine.Pin("LED", machine.Pin.OUT)
```

Compatible with:
- Pico
- Pico W
- Pico 2 W

Fallback:
```python
led = machine.Pin(25, machine.Pin.OUT)
```

---

### 🔹 Internal Temperature Sensor

```python
adc_temp = machine.ADC(4)
```

Reads RP2040 internal temperature sensor.

Temperature formula:

```
27 - (V - 0.706) / 0.001721
```

---

# 🔄 How the System Works

The program runs continuously and performs:

### 1️⃣ Non-blocking USB Command Handling

```python
poll_obj = select.poll()
```

- Avoids blocking the main loop
- Allows background tasks to run
- Improves responsiveness

---

### 2️⃣ Command Processing

Supported commands:

| Command | Action |
|----------|--------|
| `on` | Turn LED ON |
| `off` | Turn LED OFF |
| `read` | Read temperature + simulated light |
| `stream start` | Start periodic data streaming |
| `stream stop` | Stop streaming |

---

### 3️⃣ Streaming Mode

When streaming is enabled:

```
STREAM: {'temp': 28.1, 'light': 512, 'output': 1}
```

- Sends data every 1 second
- Uses non-blocking timing
- Background execution

---

### 4️⃣ Safety Logic

```python
if get_cpu_temp() > 50:
    led.value(0)
```

Example:
- Automatic shutdown if overheating
- Demonstrates autonomous embedded behavior

---

# 📊 Application Features

✔ Command-based interface  
✔ Real-time data streaming  
✔ Event-driven architecture  
✔ Non-blocking design  
✔ Expandable for real sensors  

---

# 🚀 How to Use

1. Connect Pico via USB
2. Open Thonny (or Serial Terminal)
3. Run the script
4. Type commands in Shell

Example:

```
on
read
stream start
stream stop
off
```

---

# 🔍 Example Output

```
SYSTEM READY
Commands: on | off | read | stream start | stream stop

ACK: Output ON
DATA: {'temp': 27.6, 'light': 540}
STREAM: {'temp': 27.7, 'light': 522, 'output': 1}
```

---

# 🎯 Why This Example is Important

This demonstrates:

- Embedded command interface design
- Structured data communication
- Real-time monitoring
- Embedded + PC integration
- Basic control system architecture

---

# 🆚 USB vs Wireless Communication

Use USB for:
- Development
- Testing
- Lab environments
- Reliable data logging

Use BLE/WiFi for:
- Remote sensors
- IoT devices
- Smartphone connectivity
- Cloud systems

---

# 📌 Expandability

You can extend this module to:

- Add JSON formatting
- Add real external sensors
- Control motors / relays
- Connect to Python GUI on PC
- Implement PID control loop
- Log data to CSV

---
