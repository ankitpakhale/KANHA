# Use the official Python image from the Docker Hub
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the project files
COPY . .
# Command to run the application
CMD ["python3", "src/main.py"]
