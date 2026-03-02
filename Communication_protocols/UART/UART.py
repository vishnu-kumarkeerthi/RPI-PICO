"""
UART LOOPBACK TEST FOR PICO W
-----------------------------
HARDWARE CONNECTIONS:
1. Connect GP0 (Pin 1) directly to GP1 (Pin 2) with a wire.
   (This creates a loop: TX -> RX)

HOW TO TEST:
1. Run this script in Thonny.
2. Watch the 'Shell' window at the bottom.
3. Watch the physical LED on the Pico W.
"""

from machine import UART, Pin
import time

# --- CONFIGURATION ---
# UART0: TX=GP0 (Pin 1), RX=GP1 (Pin 2)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# LED: 'LED' for Pico W, 25 for standard Pico
led = Pin("LED", Pin.OUT)

print("SYSTEM READY: UART Loopback Test Started...")
print("Ensure GP0 and GP1 are connected!")

def process_command(command_bytes):
    """Decodes data and controls LED"""
    try:
        # specific fix: ignore empty commands caused by rapid reading
        cmd = command_bytes.decode('utf-8').strip().lower()
        if not cmd: return 
    except:
        return

    print(f"Rx (Received): {cmd}")

    if cmd == "on":
        led.value(1)
    elif cmd == "off":
        led.value(0)
    elif cmd == "toggle":
        led.toggle()
    else:
        print(f"Error: Unknown '{cmd}'")

# --- MAIN LOOP ---
while True:
    # 1. READ: Check if we received our own message
    if uart.any() > 0:
        data = uart.read()
        process_command(data)
        
    # 2. WRITE: Send a command to ourselves (Loopback)
    # We send 'toggle' so you can see the LED blink continuously
    print("Tx (Sending): toggle")
    uart.write("toggle\n") 
    
    time.sleep(1.0) # Wait 1 second