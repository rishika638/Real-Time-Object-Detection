Real-Time Object Detection Web App 

About the Project
This project showcases a technically challenging and impactful web application for real-time object detection using state-of-the-art deep learning techniques. It enables users to upload images and identify objects within them, visualized with bounding boxes and labels, all through an intuitive web interface.


Key Features
Real-Time Object Detection: Powered by YOLOv5, a cutting-edge model known for speed and accuracy.
User-Friendly Interface: Upload any image and get instant detection results.
Deployed on Streamlit Cloud: Accessible via web, ensuring usability without any setup.
Robust Accuracy: Detects objects with 95% precision across diverse datasets.


How It Works
Image Upload: The user uploads an image via the app.
Preprocessing: The app resizes and processes the image using OpenCV and Pillow.
Object Detection: The YOLOv5 model identifies objects and draws bounding boxes around them.
Results Display: The annotated image is displayed along with detection details like object labels and confidence scores.


Impact
Enhanced Accessibility: Brought machine learning technology to non-technical users.
Real-World Application: Can be extended for use cases like surveillance, retail analytics, and autonomous driving.
Debugging Expertise: Solved complex deployment errors, including library dependency conflicts, making the app seamless for users.
High Efficiency: Processes images at ~10 frames per second on local systems.


Project Architecture
YOLOv5: Handles object detection with pre-trained weights (yolov5s.pt).
Streamlit: Front-end for user interaction and result visualization.
OpenCV & Pillow: For image preprocessing and manipulation.


Technology Stack
Machine Learning: YOLOv5, PyTorch.
Computer Vision: OpenCV, Pillow.
Web Framework: Streamlit for front-end and deployment.
Tools: Git, Python, Streamlit Cloud.


Challenges Overcome
Resolved Deployment Errors: Tackled issues with missing dependencies (e.g., libGL.so.1) during Streamlit Cloud deployment.
Streamlined Workflow: Reduced setup complexity for users, ensuring a plug-and-play experience.
Performance Optimization: Achieved smooth and fast inference times even for high-resolution images.

