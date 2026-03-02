"""Supported boards:
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

Notes:
- These boards support Wi-Fi only (no Ethernet)
- Wi-Fi operates only on the 2.4 GHz band
"""

import network
import time
import rp2

# Set country code for Wi-Fi regulatory compliance
# Important in India and many other regions
rp2.country('IN')

# Wi-Fi credentials
ssid = "HOTSPOT"
password = "1234567890"

# Create WLAN object in Station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting to WiFi...")
wlan.connect(ssid, password)

# Wait until Wi-Fi is connected
while not wlan.isconnected():
    print("Waiting...")
    time.sleep(1)

# Wi-Fi connected successfully
print("Connected!")
print("IP address:", wlan.ifconfig()[0])