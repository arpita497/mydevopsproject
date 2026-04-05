# Base image of python
FROM python:3.11-slim

# Sets /app as the current working directory inside the container, if /app not present docker will create automatically.
WORKDIR /app

# Install runtime requirements (copy requirements from repo root)
RUN pwd
# Copy requirements from the build context (repo root)
COPY ./app/requirements.txt /app/requirements.txt

# Install dependencies then only we should copy app in next step; -r read dependencies from requirements.txt file
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code into the container's /app directory
# This ensures /app/app.py exists (not /app/app/app.py)
COPY ./app /app

EXPOSE 8000
CMD ["python3", "app.py"]