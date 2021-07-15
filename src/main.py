# import RFIDserialRead
import LoadcellserialRead
import CameraCapture
import CSVfunction


# Process (Trigger based)
# RFID -> Weight -> Image -> Write 
while True:
    x = input('Incoming RFID')
    rfid = '0' # placeholder
    # rfid = RFIDserialRead.write_read()
    weight = LoadcellserialRead.write_read()
    camera = CameraCapture.capture()
    CSVfunction.write_data(rfid, weight, camera)
    print(rfid, weight, camera)
