import cv2
from detection import detect_light_sources

def capture_video(ip, i):
    cap = cv2.VideoCapture(ip)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break
        light_sources = detect_light_sources(frame)
        if light_sources:
            return frame, light_sources
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
