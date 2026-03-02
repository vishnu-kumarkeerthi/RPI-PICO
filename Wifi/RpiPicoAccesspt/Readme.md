# 🌐 WiFi Access Point – Raspberry Pi Pico W / Pico 2 W

This module demonstrates how to use the Raspberry Pi Pico W / Pico 2 W as a **WiFi Access Point (AP)** with a simple web server.

Supported boards:

- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

⚠ Standard Pico (Pico H) does NOT support WiFi.

---

# 📡 What is Access Point (AP) Mode?

In Access Point mode:

- The Pico becomes a WiFi hotspot
- Other devices (phone/laptop) connect directly to it
- No external router required
- Direct device-to-device communication

---

# 🎯 When to Use AP Mode

Use Access Point mode when:

- No router is available
- Direct control from phone/laptop is required
- Creating standalone embedded systems
- Field deployment applications
- Configuration portals for IoT devices

Example:
- Smart switch setup page
- IoT device configuration
- Local control dashboard

---

# 🆚 WiFi vs BLE vs USB

| Feature | WiFi AP | BLE | USB |
|----------|----------|------|------|
| Range | Long (10–50m) | Short | Cable only |
| Speed | High | Medium | High |
| Internet Access | Optional | ❌ | ❌ |
| Multiple Clients | ✅ | Limited | ❌ |
| Direct Browser UI | ✅ | ❌ | ❌ |

WiFi AP allows:
- Control via web browser
- No additional apps required
- Multiple device connections

---

# 📂 File Overview

```
Wifi/
 └── accesspt.py
```

---

# 🧠 Code Explanation

This script performs:

1. Sets WiFi country
2. Enables Access Point mode
3. Creates WiFi hotspot
4. Starts HTTP server
5. Controls LED via web interface

---

# ⚙️ WiFi Setup

### 🔹 Set Country

```python
rp2.country('IN')
```

Sets regulatory domain (important for radio rules).

---

### 🔹 Enable Access Point Mode

```python
ap = network.WLAN(network.AP_IF)
ap.active(True)
```

Enables AP mode.

---

### 🔹 Configure SSID & Password

```python
ap.config(essid="vishnu", password="23M1152")
```

Requirements:
- Password must be at least 8 characters.

---

# 🌍 Web Server Implementation

The script creates a simple HTTP server:

```python
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
```

Port 80 → Standard HTTP port.

### 🔹 Accept Client Connection

```python
cl, addr = s.accept()
```

### 🔹 Read Browser Request

```python
request = cl.recv(1024).decode()
```

### 🔹 Control LED Based on URL

If browser visits:

```
http://<IP>/on
```

LED turns ON.

If browser visits:

```
http://<IP>/off
```

LED turns OFF.

---

# 💡 HTML Interface

The Pico sends a simple webpage:

```html
<a href="/on"><button>LED ON</button></a>
<a href="/off"><button>LED OFF</button></a>
```

This creates two buttons in the browser.

---

# 🔌 Hardware Compatibility

| Feature | Pico W | Pico 2 W |
|----------|----------|------------|
| WiFi | ✅ | ✅ |
| AP Mode | ✅ | ✅ |
| BLE | ✅ | ✅ |
| Standard Pico | ❌ | ❌ |

---

# 🚀 How to Use

1. Upload script to Pico W / Pico 2 W
2. Run script
3. Connect phone/laptop to WiFi:
   - SSID: vishnu
   - Password: 23M1152
4. Open browser
5. Enter displayed IP address
6. Use buttons to control LED

---

# 📊 Expected Output

In Thonny Shell:

```
Access Point started
IP address: 192.168.4.1
Open this IP in browser: 192.168.4.1
```

---

# 🎯 Advantages of This Approach

- No router required
- No mobile app required
- Direct embedded web server
- Real-time control
- Expandable for dashboards

---

# 🔮 Possible Extensions

You can extend this example to:

- Add sensor data display
- Add JSON API
- Add password-protected login
- Create configuration portal
- Add multiple control outputs
- Connect to cloud after configuration

---

# 📌 Practical Applications

- Smart home devices
- IoT configuration pages
- Local monitoring systems
- Industrial control panels
- Remote actuator control

---

**Designed for standalone WiFi-based embedded control systems.**
