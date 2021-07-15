from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

# file_path is fixed
def capture():
    try:
        file_name = str(datetime.datetime.now().strftime("%d%m%y-%H%M%S")) + '.jpg'
        path = '/home/pi/Desktop/data/image/' + file_name
        camera.start_preview()
        sleep(5)
        camera.capture(path)
        camera.stop_preview()
        
        return path
    except:
        return False
    
def test():
    while True:
        camera.start_preview()
        try:
            pass
        except KeyboardInterrupt:
            camera.stop_preview()
            
