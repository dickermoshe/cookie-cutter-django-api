# Use the official Python image as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install PostgreSQL development libraries and headers
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Copy the poetry files to the container
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry install  --no-root --only main

# Copy the rest of the application code to the container
COPY . .

# Expose port 80 for Gunicorn
EXPOSE 80

# Start Gunicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:80", "refuah_backend.wsgi"]