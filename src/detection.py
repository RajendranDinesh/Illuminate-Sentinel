import cv2

def detect_light_sources(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the grayscale frame to detect light sources
    ret, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded frame
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    light_sources = []
    # Draw bounding boxes around the contours
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h > 50: # area threshold
            light_sources.append((x, y, x+w, y+h))
    return light_sources
