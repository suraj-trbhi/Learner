# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Create a non-root user
RUN adduser --disabled-password --gecos '' calculator-user

# Install system dependencies for potential web interface
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY calculator.py main.py web_calculator.py ./
COPY templates/ ./templates/

# Change ownership of the app directory to the non-root user
RUN chown -R calculator-user:calculator-user /app

# Switch to non-root user
USER calculator-user

# Expose port for web interface
EXPOSE 8080

# Set default command to run the web calculator
CMD ["python", "web_calculator.py"]

# Health check for web interface
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/api/health || exit 1
