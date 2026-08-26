from machine import Pin, UART
import utime

uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1,
            tx=Pin(0), rx=Pin(1))

while True:
    uart.write("U")
    utime.sleep(1)