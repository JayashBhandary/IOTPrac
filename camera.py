from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

sleep(2)

camera.capture('/home/pi/picture/newimage.jpg')
camera.stop_preview()


#Video Capture
import picamera
import time

camera = picamera.PiCamera()

try:
    camera.resolution = (1280, 720)
    camera.start_recording('video.h264')
    camera.wait_recording(10)
    camera.stop_recording()
finally:
    camera.close()