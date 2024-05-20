import cv2

from posture_detector import PostureDetector


def test_posture_detector():
    # Initialize the posture detector
    posture_detector = PostureDetector()

    # Load test images
    default_image = cv2.imread('default_posture.jpg')
    slouch_image = cv2.imread('slouch_posture.jpg')

    # Detect posture in the default posture image
    default_posture_result = posture_detector.detect_posture(default_image)
    print(f"Default Posture: {default_posture_result}")

    # Detect posture in the slouch posture image
    slouch_posture_result = posture_detector.detect_posture(slouch_image)
    print(f"Slouch Posture: {slouch_posture_result}")

    # Assertions for test results
    assert default_posture_result == "Good posture", "Default posture test failed!"
    assert slouch_posture_result == "Slouch detected", "Slouch posture test failed!"

    print("All tests passed.")


if __name__ == "__main__":
    test_posture_detector()
