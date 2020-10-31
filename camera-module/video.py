import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1920, 1080) # (64, 64) ~ (1920, 1080) px
camera.framerate = 30 # 1 ~ 30 fps

camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
