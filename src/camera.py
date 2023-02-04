import cv2
import datetime
from detection import detect_light_sources
import moviepy.editor as mp

    

def capture_video(ip, i):
    # Open a connection to the video file
    cap = cv2.VideoCapture(ip)

    while True:

        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        light_sources = detect_light_sources(frame)

        if light_sources:
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')

            date = datetime.datetime.now()
            time = date.strftime("%d-%m-%Y_%H-%M-%S")
            name = f"E:/ForestProject/data/videos/camera_{i}_{time}.mp4"

            video_writer = cv2.VideoWriter(name, fourcc, 30, (frame.shape[1], frame.shape[0]))

            start_time = datetime.datetime.now()
            while (datetime.datetime.now() - start_time).seconds < 5:
                ret, frame = cap.read()
                video_writer.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            cap.release()
            video_writer.release()
            cv2.destroyAllWindows()

            
            return f"E:/ForestProject/data/videos/camera_{i}_{time}.mp4", time
   
    cap.release()
    cv2.destroyAllWindows()
