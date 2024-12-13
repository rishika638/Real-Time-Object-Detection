
# Start with a lightweight Python base image
FROM python:3.9-slim

# Install system dependencies needed by OpenCV (libGL.so.1, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

# Set the working directory for your app
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other application files into the container
COPY . .

# Command to run the app
CMD ["streamlit", "run", "app.py"]

