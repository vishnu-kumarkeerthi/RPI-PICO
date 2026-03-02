import network
import socket
import rp2
from machine import Pin

# Set country
rp2.country('IN')

# Start Access Point mode
ap = network.WLAN(network.AP_IF)
ap.active(True)

# Configure WiFi name and password
ap.config(essid="vishnu", password="23M1152")  # Password must be 8+ chars

print("Access Point started")
print("Connect to WiFi: vishnukumar")
print("Password: password")
print("IP address:", ap.ifconfig()[0])

# LED
led = Pin("LED", Pin.OUT)

# Simple web server
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Open this IP in browser:", ap.ifconfig()[0])

while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()

    if "/on" in request:
        led.value(1)
    if "/off" in request:
        led.value(0)

    response = """\
HTTP/1.1 200 OK

<html>
    <body>
        <h1>Pico W Access Point</h1>
        <p>
            <a href="/on"><button>LED ON</button></a>
            <a href="/off"><button>LED OFF</button></a>
        </p>
    </body>
</html>
"""

    cl.send(response)
    cl.close()

