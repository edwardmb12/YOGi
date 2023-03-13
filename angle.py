from math import atan2, degrees, fabs

def getAngle(firstPoint, midPoint, lastPoint):
    result = degrees(atan2(lastPoint.position.y - midPoint.position.y,
                           lastPoint.position.x - midPoint.position.x)
                     - atan2(firstPoint.position.y - midPoint.position.y,
                             firstPoint.position.x - midPoint.position.x))
    result = fabs(result) # Angle should never be negative
    if result > 180:
        result = 360.0 - result # Always get the acute representation of the angle
    return result

right_shoulder_landmark = pose.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER]
right_hip_landmark = pose.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP]
right_knee_landmark = pose.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE]

rightHipAngle = getAngle(right_shoulder_landmark, right_hip_landmark, right_knee_landmark)

