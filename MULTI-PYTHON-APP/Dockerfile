# Stage 1: Build the application
FROM python:3.9 AS builder

# Set working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Stage 2: Create the final lightweight image
FROM python:3.9-slim AS runtime

# Set working directory in the container
WORKDIR /app

# Copy the installed dependencies and application code from the builder stage
COPY --from=builder /app /app

# Command to run the application
CMD ["python", "guessing_game.py"]