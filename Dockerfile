# Use a lightweight Python base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual application code
COPY app.py .

# Open port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
