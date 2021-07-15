#!/usr/bin/env python3
# todo: create a lookup table function for comparison
# csv or postgres also fine

import time
import serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 19200, # as per report by KiatNern
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

# rudimentary soln to identify based on unique key in string
# todo: explore the different types of possible inputs 
def write_read():
    while True:
        x = ser.readline()
        if len(x) != 0: # incoming byte available, then process
            break
    for i in x:
        if i == 105: # temp soln to tag to id1
            print('id1')
            return 'id1'
        elif i == 115: # temp soln to tag to id2
            print('id2')
            return 'id2'
            
