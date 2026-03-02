"""This program reads an analog voltage connected to GPIO26 (ADC0)
and converts the raw ADC value into a voltage level.

Hardware notes:
- GPIO26 is ADC0 on all RP2040-based boards
- ADC input range: 0V to 3.3V ONLY
- Do NOT exceed 3.3V on the ADC pin """


from machine import Pin, ADC
import time

adc = ADC(Pin(26))

conversion_factor = 3.3 / 65535

print("Analog voltage Reading on ADC pin")

while True:
    raw = adc.read_u16()
    voltage = raw * conversion_factor
    print("Raw ADC:",raw,"Voltage:",voltage,"V")
    time.sleep(0.5)
