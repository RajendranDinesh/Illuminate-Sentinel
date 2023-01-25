import cv2

# Load the video
video = cv2.VideoCapture("E:/ForestProject/data/videos/test.mp4")

# Get the first frame
ret, frame = video.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set a threshold for the frame
threshold = 250

# Create a background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read the next frame
    ret, frame = video.read()

    # Exit the loop if there are no more frames
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get the foreground mask using the background subtractor
    foreground_mask = bg_subtractor.apply(gray)

    # Apply threshold to the mask
    _, thresholded = cv2.threshold(foreground_mask, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded mask
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours
    for contour in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Draw the bounding rectangle on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
video.release()

# Close all windows
cv2.destroyAllWindows()
