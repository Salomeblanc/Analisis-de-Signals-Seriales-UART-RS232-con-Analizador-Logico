    from machine import Pin, UART
import utime

uart = UART(0, baudrate=57600, bits=8, parity=1, stop=1,
            tx=Pin(0), rx=Pin(1))

while True:
    uart.write("UMNG_2026_LIDER_EN_TELECOMUNICACIONES")
    utime.sleep(1)