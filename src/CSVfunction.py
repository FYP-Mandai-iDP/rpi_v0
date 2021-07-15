import csv
import datetime
import time
import os

def write_data(rfid, x, y):

    output_file = '/home/pi/Desktop/data/data.csv'

    if os.path.isfile(output_file):
        print("File Exist")
        print("Writing to existing file")
        with open(output_file, 'a', newline='') as csvfile:
            fieldnames = ['timestamp', 'rfid', 'weight', 'image']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({'timestamp':datetime.datetime.now().strftime("%c"),'rfid': rfid, 'weight': x, 'image': y})
                            
    else:
        print("File does not exist")
        print("Creating new file")
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'rfid', 'weight', 'image']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerow({'timestamp':datetime.datetime.now().strftime("%c"),'rfid': rfid, 'weight': x, 'image': y})
