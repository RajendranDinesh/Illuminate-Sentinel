import camera
import alert
import database
import time
from multiprocessing import Process

# List of camera IP addresses
cameras = [0]

def detect_light_source(i, video_path, time):
    alert.send_alert(i, video_path, time)

def capture_and_alert(i, ip):
    while True:
        video_path, time = camera.capture_video(ip,i)
        if video_path:
            # Save video in the database
            video_id = database.save_video(video_path)
            # Start a new process to continuously detect light sources in the video
            process = Process(target=detect_light_source, args=(i, video_path, time))
            process.start()

if __name__ == '__main__':
    processes = []
    for i, ip in enumerate(cameras):
        process = Process(target=capture_and_alert, args=(i, ip))
        process.start()
        processes.append(process)
    while True:
        time.sleep(1)