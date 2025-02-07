# Use Python 3.9 as the base image
FROM python:3.13.1-slim

# Set the working directory
WORKDIR /

# Copy the requirements file
COPY requirements.txt .

# Update pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY preprocess_service.py .

# Expose the service port
EXPOSE 5001

# Run the application
CMD ["python", "preprocess_service.py"]
