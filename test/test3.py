import cv2

# Initialize the video capture object
cap = cv2.VideoCapture("E:/ForestProject/data/videos/test.mp4")
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors that represent artificial light
    lower_light = (55, 55, 55)
    upper_light = (255, 255, 255)

    # Create a mask that filters out everything except the artificial light
    mask = cv2.inRange(hsv, lower_light, upper_light)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for contour in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Check if the width and height of the bounding rectangle are within a certain range
        if w > 10 and h > 10:
            # Draw a rectangle around the contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the frame with the boxes
    cv2.imshow("Light Detection", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
