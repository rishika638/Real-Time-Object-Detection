import streamlit as st
import cv2
import torch
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

st.title("Real-Time Object Detection")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    # Read the image
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Run detection
    results = model(image)
    st.write(results.pandas().xyxy[0])  # Display detection results
    st.image(results.render()[0], caption="Detected Image", use_column_width=True)
