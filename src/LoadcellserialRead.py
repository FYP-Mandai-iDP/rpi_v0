#!/usr/bin/env python3
import time
import serial
# Basic functionality for Arduino based loadcell reading
# Have issues with the creeping

arduino = serial.Serial(
    port = '/dev/ttyACM0',
    baudrate = 9600, # Communication with Arduino
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

# Write 'r' to arduino to request for weight
def write_read():
    arduino.write(bytes('r','utf-8'))
    time.sleep(0.5)
    data = arduino.readline().decode('utf-8').rstrip()
    return data

# Python level processing of averaging weight over time
def get_average(n = 10):
    lst = []
    for i in range(n):
        value = write_read()
        lst.append(float(value))
    return round( (sum(lst) / n), 2)

# Write 't' to Tare the the weight
def tare():
    arduino.write(bytes('t','utf-8'))
    time.sleep(0.5)
    data = arduino.readline().decode('utf-8').rstrip()
    return data

# For testing
def interface(): # automated
    while True:
        cmd = input('Enter\t')
        if cmd == 'r':
            value = write_read()
        elif cmd == 'a':
            value = get_average()
        elif cmd == 't':
            value = tare()
            
        print(value)
        
        
        
# Setup time    
time.sleep(5) 
print('Loadcell Read')

# Driver Code
#interface()