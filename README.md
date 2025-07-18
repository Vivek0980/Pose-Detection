# Real-Time Human Pose Detection using MediaPipe and OpenCV

This project demonstrates how to perform real-time human pose detection on a video using Google's MediaPipe and OpenCV in Python.

## 📌 Features
- Detects and draws 33 human body landmarks
- Displays real-time FPS (Frames Per Second)
- Overlays keypoint circles on body joints
- Processes input from a video file (can be adapted to webcam)

## 🧰 Requirements
- Python 3.7+
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)

## 📂 File Structure
- `pose_detect.py`: Main script for pose detection
- `video.mp4`: Input video file (replace with your path)

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

2. Replace the video path in the script:
   ```python
   video = cv2.VideoCapture("your_video_path.mp4")
   ```

3. Run the script:
   ```bash
   python pose_detect.py
   ```

4. Press `q` to quit the video window.

## 📌 Notes
- The video is resized to 700x700 for consistent display.
- Each landmark is drawn with a yellow circle.
- FPS is shown at the top-left for performance insight.

## 📷 Output Example
Displays the video frame with pose skeleton drawn in real time.

## 🧠 Based On
- [MediaPipe Pose Documentation](https://google.github.io/mediapipe/solutions/pose)
- OpenCV official documentation

## ✍️ Author
Vivek Nani
