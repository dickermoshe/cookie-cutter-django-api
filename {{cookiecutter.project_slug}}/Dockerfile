# Use the official Python image as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install PostgreSQL development libraries and headers
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Install Poetry
RUN pip install poetry
RUN pip install poetry-plugin-export

# Copy the poetry files to the container
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry export -f requirements.txt -o requirements.txt --without-hashes
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 80 for Gunicorn
EXPOSE 80


# Run collectstatic
# RUN poetry run python manage.py collectstatic --noinput

# Run migrations
# RUN poetry run python manage.py migrate

# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80","--timeout","600", "{{cookiecutter.project_slug}}.wsgi"]