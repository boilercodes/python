FROM python:3.9-slim

# Set pip to have cleaner logs and no saved cache
ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry.
RUN pip install --upgrade poetry

WORKDIR /app

# Copy dependencies and lockfile.
COPY pyproject.toml poetry.lock /app/

# Install dependencies and lockfile, excluding development dependencies.
RUN poetry install --no-dev --no-interaction

# Copy the rest of the project code
COPY . .

# Start the bot
CMD ["python", "-m", "app"]

# Define docker persistent volumes
VOLUME /app/app/logs
