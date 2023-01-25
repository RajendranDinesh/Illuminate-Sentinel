import cv2

# Initialize the video capture
cap = cv2.VideoCapture('http://10.40.27.82:8080/videofeed')

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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the frame with boxes
    cv2.imshow("Frame", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
