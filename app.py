import streamlit as st
import cv2
import torch
import numpy as np
from pathlib import Path

# Clone YOLOv5 repo if it's not already cloned
yolov5_dir = Path('yolov5')
if not yolov5_dir.exists():
    import os
    os.system('git clone https://github.com/ultralytics/yolov5')

# Import YOLOv5 code
from yolov5 import YOLOv5

# Load model
model = YOLOv5('yolov5s.pt')  # Path to the model (use the .pt file)

st.title("Real-Time Object Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Detection
    results = model(image)
    st.write(results.pandas().xyxy[0])
    st.image(results.render()[0], caption="Detected Image", use_column_width=True)
