# Base image
FROM python:3.11-bullseye

# Set work directory
WORKDIR /app

# Install system dependencies (including distutils)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy UI requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy UI code
COPY . .

# Expose Gradio port
EXPOSE 7860

# Start Gradio UI
CMD ["python", "gradio_app.py"]
