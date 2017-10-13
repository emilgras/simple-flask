# Use an official Python runtime as a parent image
FROM python:3-slim


# Crete a working directory
WORKDIR /app


# Copy /app % requirements.txt into th containers working directory
COPY app/ .
COPY requirements.txt .


RUN pip install -r requirements.txt


# specify the port number the container should expose
EXPOSE 5000


# Run app.py when the container launches
CMD python app.py
