import camera
import alert
import database
import time
from multiprocessing import Process

# List of camera IP addresses
#cameras = ["rtsp://username:password@192.168.0.1:554/stream", "rtsp://username:password@192.168.0.2:554/stream"]
cameras = ['https://10.10.74.198:8080/videofeed']

def capture_and_alert(i, ip):
    while True:
        video_path, time = camera.capture_video(ip,i)
        if video_path:
            # Save video in the database
            video_id = database.save_video(video_path)
            # Send alert with video and video_id
            alert.send_alert(i, video_path, time)

if __name__ == '__main__':
    processes = []
    for i, ip in enumerate(cameras):
        process = Process(target=capture_and_alert, args=(i, ip))
        process.start()
        processes.append(process)
    while True:
        time.sleep(1)
