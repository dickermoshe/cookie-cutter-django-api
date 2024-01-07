# Use the official Python image as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install PostgreSQL development libraries and headers
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/index/bash_history/.bash_history" \
    && echo "$SNIPPET" >> "/root/.bashrc"

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


# Run collectstatic
# RUN poetry run python manage.py collectstatic --noinput

# Run migrations
# RUN poetry run python manage.py migrate

# Start Gunicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:80", "{{cookiecutter.project_slug}}.wsgi"]