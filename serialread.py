import time
import serial
import numpy as np
from time import sleep, strftime, time

ser=serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=9999999
    )

count = 1
with open("/home/pi/drape_weights.csv", "a") as log:
    while True:
        while count % 7 == 0:
            count += 1
            x = ser.readline()
            y = x.split()
            print (y)
            log.write("{0}\n".format(y))                 
                 
        else:
            count += 1
            x = ser.readline()
            y = x.split()
            print(y)
            log.write("{0}\t".format(y))
            