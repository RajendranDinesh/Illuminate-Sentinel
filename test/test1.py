import cv2
import datetime

# Initialize the video capture
cap = cv2.VideoCapture("https://192.168.43.134:8080/videofeed")

name = f"E:/ForestProject/data/videos/test5.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video_writer = cv2.VideoWriter(name, fourcc, 30, (1920, 1080))

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use a threshold to detect bright pixels
    thresh = cv2.threshold(gray, 20, 250, cv2.THRESH_BINARY)[1]

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # Draw a box around each contour
    for c in contours:
        if cv2.contourArea(c) > 100:
            (x, y, w, h) = cv2.boundingRect(c)
            if h>10 and w>10:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the frame with boxes
    #cv2.imshow("Frame", frame)
    video_writer.write(frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()