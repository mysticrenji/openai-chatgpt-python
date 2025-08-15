# Start with python 3.9 base image
FROM python:3.13.6-slim

# Set working directory in docker container
WORKDIR /app

# Copy requirements.txt to /app directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy python files to /app directory
COPY *.py .

# Run the python program
ENTRYPOINT ["python", "play-openai.py"]
