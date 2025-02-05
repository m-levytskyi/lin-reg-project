# Use an official Python runtime as a parent image
FROM python:3.13.1-slim

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container
COPY . /

# Update pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "lin_reg.py"]
