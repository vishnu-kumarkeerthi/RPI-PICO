"""
Generic USB Command & Streaming Interface (MicroPython)

Supported boards:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W
- RP2040 reference boards (e.g. Rhodium)

Features:
- USB (CDC) command interface
- LED / actuator control
- Single-shot sensor read
- Periodic data streaming
- Non-blocking input handling
"""

import sys
import select
import machine
import time
import random

# -------------------------------------------------
# HARDWARE CONFIGURATION (GENERIC)
# -------------------------------------------------

# Onboard LED (Pico / Pico W / Pico 2 W compatible)
try:
    led = machine.Pin("LED", machine.Pin.OUT)
except Exception:
    # Fallback for custom boards
    led = machine.Pin(25, machine.Pin.OUT)

# Internal temperature sensor (RP2040 ADC4)
adc_temp = machine.ADC(4)

# -------------------------------------------------
# APPLICATION VARIABLES
# -------------------------------------------------
stream_mode = False
last_stream_time = 0
stream_interval = 1000   # ms (1 second)

# -------------------------------------------------
# USB (CDC) INPUT SETUP
# -------------------------------------------------
poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------
def get_cpu_temp():
    """
    Read RP2040 internal temperature sensor.
    Valid on Pico / Pico W / Pico 2 W.
    """
    reading = adc_temp.read_u16() * (3.3 / 65535)
    temperature = 27 - (reading - 0.706) / 0.001721
    return round(temperature, 2)

def get_simulated_light():
    """
    Simulated sensor value (replace with real ADC later).
    """
    return random.randint(200, 800)

def process_command(command):
    """
    Process incoming USB commands.
    """
    global stream_mode, stream_interval
    cmd = command.lower().strip()
    if not cmd:
        return

    if cmd == "on":
        led.value(1)
        print("ACK: Output ON")

    elif cmd == "off":
        led.value(0)
        print("ACK: Output OFF")

    elif cmd == "read":
        t = get_cpu_temp()
        l = get_simulated_light()
        print(f"DATA: {{'temp': {t}, 'light': {l}}}")

    elif cmd == "stream start":
        stream_mode = True
        print("ACK: Streaming Started")

    elif cmd == "stream stop":
        stream_mode = False
        print("ACK: Streaming Stopped")

    else:
        print(f"ERROR: Unknown command '{cmd}'")

# -------------------------------------------------
# SYSTEM READY
# -------------------------------------------------
print("SYSTEM READY")
print("Commands: on | off | read | stream start | stream stop")

# -------------------------------------------------
# MAIN LOOP
# -------------------------------------------------
while True:

    # 1️⃣ Non-blocking USB command handling
    if poll_obj.poll(0):
        line = sys.stdin.readline()
        if line:
            process_command(line)

    # 2️⃣ Background streaming task
    if stream_mode:
        now = time.ticks_ms()
        if time.ticks_diff(now, last_stream_time) > stream_interval:
            t = get_cpu_temp()
            l = get_simulated_light()
            print(f"STREAM: {{'temp': {t}, 'light': {l}, 'output': {led.value()}}}")
            last_stream_time = now

    # 3️⃣ Safety / autonomous logic
    if get_cpu_temp() > 50:
        led.value(0)  # Emergency shutdown example

    time.sleep(0.01)
