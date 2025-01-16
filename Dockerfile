# Use the official Python 3.12.8 slim image as the base image
FROM python:3.12.8-slim-bullseye

# Set environment variables to improve Python behavior
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /code

# Install Python dependencies
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /code/
