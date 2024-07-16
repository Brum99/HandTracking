import cv2  # OpenCV for video capture and image processing
import mediapipe as mp  # MediaPipe for hand tracking
import time  # Time module (you can use this for measuring performance, not used in this code)

# Initialize video capture object (0 typically refers to the default camera)
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands solution
mpHands = mp.solutions.hands

# Create a Hands object to perform hand tracking
hands = mpHands.Hands()

# Infinite loop to continuously capture frames from the camera
while True:
    # Capture a frame from the camera
    success, img = cap.read()

    # Convert the frame from BGR (default in OpenCV) to RGB (required by MediaPipe)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hands and hand landmarks
    results = hands.process(imgRGB)
    
    # Print the detected hand landmarks (if any) to the console
    print(results.multi_hand_landmarks)

    # Display the frame with any annotations (if added, not done in this code)
    cv2.imshow("Image", img)
    
    # Wait for a short period to allow the image to be displayed, 1ms here
    # This also allows for breaking the loop by pressing a key (not implemented in this code)
    cv2.waitKey(1)
