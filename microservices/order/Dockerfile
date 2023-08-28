# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY order.py /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 9090 available to the world outside this container
EXPOSE 9090

# Define environment variables
ARG GIT_COMMIT
ENV CONSUMER_KEY='ck_d7f5321f54f51056c0189da9fb9c168c1f1d9855'
ENV CONSUMER_SECRET='cs_53d437498032ccd27db4452eaa6fb6fbc8180886'
ENV API_URL='http://192.168.10.10:8080'
ENV NAME World

LABEL git_commit=$GIT_COMMIT

# Run the command to start the order.py script
CMD ["python", "order.py"]
