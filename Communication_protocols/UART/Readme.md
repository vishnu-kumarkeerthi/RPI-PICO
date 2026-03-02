# 🔁 UART Communication – Raspberry Pi Pico Series

This folder demonstrates **UART (Universal Asynchronous Receiver Transmitter)** communication using a **Loopback Test**.

Supported boards:

- Raspberry Pi Pico H
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

---

# 📡 What is UART?

UART is a simple asynchronous serial communication protocol.

### 🔹 UART Lines
- **TX** – Transmit
- **RX** – Receive

Unlike I2C or SPI, UART:
- Does NOT use a clock line
- Requires matching baud rate on both sides
- Uses start/stop bits for synchronization

---

# 🎯 Typical Use Cases

- GPS modules
- GSM modules
- Bluetooth modules
- Serial debugging
- Communication between two microcontrollers

---

# 🔄 UART Loopback Test

This example demonstrates a **loopback test**.

### 🔌 Hardware Connection

Connect:

```
GP0 (TX) → GP1 (RX)
```

This means:
- The data sent (TX) is immediately received (RX)
- The board talks to itself

---

# 📂 File Overview

```
UART/
 ├── UART.py   (Loopback test script)
```

---

# 📄 Code Explanation

## 🔹 UART Initialization

```python
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
```

- Uses UART0 controller
- Baudrate: 9600
- TX → GP0
- RX → GP1

---

## 🔹 LED Configuration

```python
led = Pin("LED", Pin.OUT)
```

- Pico W → `"LED"`
- Standard Pico → `Pin(25)`
- Pico 2 W → `"LED"`

---

## 🔹 Command Processing

The function:

```python
def process_command(command_bytes):
```

- Decodes received UART data
- Converts to lowercase
- Controls LED based on command

Supported commands:

- `"on"` → LED ON
- `"off"` → LED OFF
- `"toggle"` → Toggle LED

---

## 🔹 Main Loop Operation

The loop performs two operations:

### 1️⃣ READ

```python
if uart.any() > 0:
    data = uart.read()
```

- Checks if data is received
- Reads incoming bytes
- Processes command

### 2️⃣ WRITE

```python
uart.write("toggle\n")
```

- Sends "toggle" command
- Because TX and RX are connected,
  the same message is received back

### Result:
LED toggles every second.

---

# ⚙️ Board Configuration

| Feature | Pico H | Pico W | Pico 2 W |
|----------|----------|----------|------------|
| UART Support | ✅ | ✅ | ✅ |
| UART Controllers | 2 | 2 | 2 |
| Default Logic | 3.3V | 3.3V | 3.3V |

No code changes required between boards.

---

# 🔌 Default UART Pins

| UART | TX | RX |
|-------|------|------|
| UART0 | GP0 | GP1 |
| UART1 | GP4 | GP5 |

You can reassign pins if needed:

```python
uart = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
```

---

# 🧠 Important UART Concepts

### 🔹 Baud Rate
- Defines communication speed
- Both sides must match
- Common values: 9600, 115200

### 🔹 Start & Stop Bits
UART frames include:
- Start bit
- Data bits
- Optional parity
- Stop bit

---

# 🛠 How to Test

1. Connect GP0 → GP1
2. Run script in Thonny
3. Observe:
   - Shell output (Tx / Rx messages)
   - Physical LED toggling

Expected Output:

```
Tx (Sending): toggle
Rx (Received): toggle
```

LED blinks every 1 second.

---

# 🚀 Why Use Loopback Test?

- Verify UART hardware functionality
- Test TX and RX pins
- Validate baud rate configuration
- Confirm data encoding/decoding

---

# 🎯 Purpose of This Module

- Understand serial communication basics
- Learn how to configure UART
- Control hardware via serial commands
- Prepare for real external module integration

-
