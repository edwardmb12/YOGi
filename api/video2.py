import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def classify_pose(pose_landmarks):

    # # Classify pose
        # if results.pose_landmarks is not None:
        #     # Your code to classify the pose here
        #     pass

         # Extract landmarks
        # try:
        #     landmarks = results.pose_landmarks.landmark

        #     # Get coordinates
        #     shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        #     elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        #     wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        #     # Calculate angle
        #     angle = calculate_angle(shoulder, elbow, wrist)

        #     # Visualize angle
        #     cv2.putText(image, str(angle),
        #                    tuple(np.multiply(elbow, [640, 480]).astype(int)),
        #                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
        #                         )

        # except:
        #     pass
    pass

def webcam():

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    cap.release()
    cv2.destroyAllWindows()

    # Initialize mediapipe pose - Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            # Read feed from webcam
            ret, frame = cap.read()
            cv2.imshow('Mediapipe Feed', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

            # Convert feed to RGB format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Process pose detection
            results = pose.process(image)

            # Draw pose landmarks on image
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                    )

            # Display image
            #cv2.imshow('Mediapipe Feed', image)
            st.image(image, channels="BGR")

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release webcam and close windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
