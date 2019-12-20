from time import sleep
from picamera import PiCamera

camera = PiCamera()

camera.resolution = (3280,2464)

'''camera.start_preview()'''


sleep(1)
for filename in camera.capture_continuous('timelapse/img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(120) # wait 5 minutes
