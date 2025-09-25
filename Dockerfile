FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y wget procps && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Flask & psutil
RUN pip install flask psutil

# Copy files
COPY . .

# Jalankan Flask di port 80
CMD ["python", "app.py"]
