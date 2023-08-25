# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY product.py /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV CONSUMER_KEY=ck_871224cf87f8459b0862453fa7e03dbe2accbecd
ENV CONSUMER_SECRET=cs_3f3dc3a74524e7f7442303a6e12ec03de5da505c

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "product.py"]