import camera
import alert
import database

# List of camera IP addresses
cameras = ["rtsp://username:password@192.168.0.1:554/stream", "rtsp://username:password@192.168.0.2:554/stream"]

cameras = [0]

while True:
    for i, ip in enumerate(cameras):
        video_path = camera.capture_video(ip,i)
        if video_path:
            # Save video in the database
            video_id = database.save_video(video_path)
            # Send alert with video and video_id
            #alert.send_alert(i, video_path, video_id)
