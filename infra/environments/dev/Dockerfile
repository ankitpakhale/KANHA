# use the official python image from docker hub
FROM python:3.9-slim

# set the working directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the project files
COPY . .

# ensure the entrypoint script has execute permissions
RUN chmod +x entrypoint.sh

# expose port 7010 for the application
EXPOSE 7010

# set the default command to start the server on port 7010
CMD ["python3", "app/main.py", "--port", "7010"]
