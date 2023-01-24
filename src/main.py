from camera import capture_video
from detection import detect_light_sources
from alert import send_alert
from database import store_image_path
import datetime
import cv2

#camera_ips = ['rtsp://192.168.1.101:554/user=admin&password=&channel=1&stream=0.sdp',
#              'rtsp://192.168.1.102:554/user=admin&password=&channel=1&stream=0.sdp',
#              'rtsp://192.168.1.103:554/user=admin&password=&channel=1&stream=0.sdp']

camera_ips = [0]

for i, ip in enumerate(camera_ips):
    frame, light_sources = capture_video(ip, i)
    if light_sources:
        timestamp = datetime.datetime.now()
        image_path = f"E:\ForestProject\data\images\camera_{i}_{timestamp}.jpg"
        cv2.imwrite(image_path, frame)
        #send_alert(i, image_path, timestamp)
        #store_image_path(image_path)
