FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY setup_bot.py .
COPY server_config.py .

# Create volume mount point for .env file
VOLUME ["/app/config"]

# Run the bot
CMD ["python", "-u", "setup_bot.py"]
