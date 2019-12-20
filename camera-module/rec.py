import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1920,1080)

camera.capture('abc.jpg')




camera.start_preview()
time.sleep(3)
camera.stop_preview()
'''


camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()

'''
