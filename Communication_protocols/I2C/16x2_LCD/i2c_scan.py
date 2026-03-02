"""
Generic I2C Scan Code for RP2040 Boards (MicroPython)

Compatible with:
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W
- Rhodium board 

I2C configuration used:
- I2C Bus  : I2C1
- SDA Pin  : GPIO2
- SCL Pin  : GPIO3
- Frequency: 100 kHz
"""

from machine import Pin, I2C
import time

# -------------------------------
# I2C CONFIGURATION (CHANGE HERE)
# -------------------------------
I2C_BUS_ID = 1          # I2C0 or I2C1
I2C_SDA_PIN = 2         # GPIO2
I2C_SCL_PIN = 3         # GPIO3
I2C_FREQ = 100_000      # 100 kHz standard mode
# I2C0: SDA = GP0,4,8,12,16,20 | SCL = GP1,5,9,13,17,21
# I2C1: SDA = GP2,6,10,14,18,26 | SCL = GP3,7,11,15,19,27


# Initialize I2C
i2c = I2C(
    I2C_BUS_ID,
    sda=Pin(I2C_SDA_PIN),
    scl=Pin(I2C_SCL_PIN),
    freq=I2C_FREQ
)

print("I2C initialized")
print("Bus :", I2C_BUS_ID)
print("SDA :", "GPIO{}".format(I2C_SDA_PIN))
print("SCL :", "GPIO{}".format(I2C_SCL_PIN))
print("Freq:", I2C_FREQ, "Hz")

# Scan for I2C devices
devices = i2c.scan()

if devices:
    print("I2C device(s) found:")
    for dev in devices:
        print(" - Address:", hex(dev))
else:
    print("No I2C devices found")

