# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /code

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 7860

# Run app
CMD ["python", "app.py"]
