import cv2
import mediapipe as mp
import time


class PostureDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.slouch_threshold = 0.2  # Adjust this threshold based on experimentation
        self.last_movement_time = time.time()

    def detect_posture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates of shoulders and hips
            shoulder_left = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value]
            shoulder_right = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
            hip_left = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value]
            hip_right = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value]

            # Calculate the vertical distance between the midpoint of the shoulders and hips
            shoulder_mid_y = (shoulder_left.y + shoulder_right.y) / 2
            hip_mid_y = (hip_left.y + hip_right.y) / 2
            vertical_distance = abs(shoulder_mid_y - hip_mid_y)

            # Check if the vertical distance indicates slouching
            if vertical_distance < self.slouch_threshold:
                return "Slouch detected"
            else:
                self.last_movement_time = time.time()  # Update last movement time
                return "Good posture"

    def time_since_last_movement(self):
        return time.time() - self.last_movement_time

    def release(self):
        self.cap.release()
