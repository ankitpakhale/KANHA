# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Ensure the start script has execute permissions
RUN chmod +x start_application.sh

# Command to run the application
ENTRYPOINT ["./start_application.sh"]
