# BAST - Back Straight Tracker

BAST (Back Straight Tracker) is a desktop application designed to help users maintain good posture 
and take regular breaks. It uses the built-in webcam to monitor the user's posture and sends notifications
when slouching is detected. Additionally, it tracks sedentary periods and reminds users to take breaks 
if they have been sitting for too long.

## Features

- **Posture Detection**: Uses the webcam to detect if the user is slouching and sends a notification.
- **Sedentary Tracking**: Sends a notification to remind the user to take a break if no movement is detected within
- a configurable interval (default is 50 minutes).
- **Customizable Notifications**: Allows users to customize the notification messages and break intervals.
- **System Tray Integration**: Runs in the background and displays an icon in the system tray for easy access.

## Requirements

- Python 3.11
- `opencv-python` library
- `tkinter` library (usually included with Python)
- `pystray` library
- `Pillow` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bast.git
    cd bast
    ```

2. Install the required libraries:
    ```sh
    pip install opencv-python pystray Pillow
    ```

3. Save the logo image in the same directory as the application scripts. The image should be named `bast_icon.png`.

## Usage

1. Run the application:
    ```sh
    python bast_app.py
    ```

2. The application window will appear. You can customize the notification message and break interval from the UI.

3. The application will monitor your posture and remind you to take breaks as needed. It will minimize to the system tray when closed.

## Files

- `bast_app.py`: Main application script.
- `posture_detector.py`: Script for posture detection using OpenCV.
- `bast_icon.png`: Logo used as the application and system tray icon.

## Building the Executable

To create an executable version of the application, use PyInstaller:

```sh
pyinstaller --onefile --windowed bast_app.py
"# BAST" 
