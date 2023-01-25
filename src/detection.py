import cv2

def detect_light_sources(frame):

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the grayscale frame
    ret, thresh_frame = cv2.threshold(gray_frame, 20, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded frame
    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    light_sources = []

    # Loop through the contours
    for contour in contours:

        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the width and height of the bounding rectangle are within a certain range
        if w > 10 and h > 10:
            # Append the bounding rectangle coordinates to the light_sources list
            light_sources.append((x, y, w, h))
            
    return light_sources
