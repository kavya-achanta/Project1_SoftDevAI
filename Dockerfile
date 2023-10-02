# Start with a base Python image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements to the container
COPY requirements.txt .

# Install dependencies
RUN apt-get update && \
    apt-get install -y libglib2.0-0 && \
    apt-get install -y libgl1-mesa-glx && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the model, Flask app, and any other necessary files to the container
COPY plant_pathology_model.h5 .
COPY app.py .
COPY templates templates/

# Expose the port the app runs on
EXPOSE 443

# Set the default command to run the Flask app
CMD ["python", "app.py"]
