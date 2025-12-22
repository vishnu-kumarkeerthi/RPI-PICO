from machine import Pin
import time

LED_PIN = 25  # Built-in LED
led = Pin(LED_PIN, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
