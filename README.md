# Smart Surveillance System

## About the Project

Smart Surveillance System is a computer vision based security application that combines face recognition and real-time object tracking to make surveillance more intelligent and efficient.

The project uses a camera feed to detect and track objects in real time while also using registered face data to recognize known individuals. A web-based interface is provided to make the system easy to monitor and use.

## Features

- Real-time video surveillance
- Face detection and recognition
- Real-time object detection and tracking
- Recognition of registered/known faces
- YOLOv8-based object detection
- Web-based monitoring interface
- Organized storage for known faces
- Real-time camera feed processing

## Technologies Used

- Python
- OpenCV
- YOLOv8
- Flask
- HTML
- CSS
- JavaScript
- Face Recognition
- Computer Vision

## Project Structure

smart-surveillance-system/


├── known_faces/        # Registered face images

├── static/             # CSS, JavaScript and other static files

├── templates/          # HTML templates

├── app.py              # Main application

├── routes.py           # Application routes

├── yolo_tracker.py     # YOLO-based object detection and tracking

├── yolov8n.pt          # YOLOv8 model

├── encodings.pkl       # Stored face encodings

├── requirements.txt    # Python dependencies

└── README.md           # Project documentation

## How It Works

The system processes the camera feed in real time and performs multiple computer vision tasks.

1. The camera captures live video.
2. Video frames are processed using OpenCV.
3. YOLOv8 is used for object detection and tracking.
4. Faces are detected from the video stream.
5. Detected faces are compared with stored face encodings.
6. Registered individuals can be recognized.
7. Detected objects and faces are displayed through the surveillance interface.
8. The web application provides an interface for monitoring the system.

## Installation

### 1. Clone the Repository

git clone https://github.com/kartikpandey0-arch/smart-surveillance-system.git

### 2. Open the Project Directory

cd smart-surveillance-system

### 3. Install Dependencies

pip install -r requirements.txt

## Running the Application

Start the application using:

python app.py

Once the application starts, open the local URL provided in the terminal in your browser.

## Known Faces

The `known_faces` folder is used to store images of registered individuals.

The stored face information is processed and saved in `encodings.pkl`, which can be used by the system during face recognition.

For better recognition results, use clear and properly visible face images.

## YOLO Object Tracking

The project uses the `yolov8n.pt` YOLOv8 model for real-time object detection.

The `yolo_tracker.py` file handles the object detection and tracking functionality used by the surveillance system.

## Screenshots

Screenshots of the application interface can be added here to demonstrate the working of the Smart Surveillance System.

## Future Improvements

Some possible improvements for future versions include:

- Real-time security alerts
- Email or mobile notifications
- Suspicious activity detection
- Event and activity logging
- Database integration
- Cloud-based surveillance
- User authentication
- Improved face recognition accuracy
- Advanced object tracking
- Mobile-friendly interface

## Privacy & Responsible Use

This project is intended for educational and authorized security-monitoring purposes.

If camera surveillance or facial recognition is used in a real-world environment, ensure that the system is used responsibly and in accordance with applicable privacy and data-protection requirements.

## Author

**Kartik Pandey**

GitHub: https://github.com/kartikpandey0-arch

## Acknowledgement

This project was developed as a practical implementation of computer vision, face recognition, object detection, and real-time surveillance concepts.

---

⭐ If you find this project useful, consider giving the repository a star.
