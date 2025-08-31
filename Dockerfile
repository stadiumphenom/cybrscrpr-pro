# Use official lightweight Python image
FROM python:3.10-slim

# Prevents Python from writing .pyc files and enables unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# --- (1) System dependencies ---
# - build-essential: compile native wheels
# - espeak + libespeak1: voice support for pyttsx3/espeak
# - ffmpeg: media handling (useful if you add TTS/processing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    espeak \
    ffmpeg \
    libespeak1 \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better layer caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# --- (2) Streamlit theme/config included in image ---
# (This is redundant if already under /app, but explicit is nice)
COPY .streamlit /app/.streamlit

# Expose Streamlit port
EXPOSE 8501

# Streamlit runtime defaults
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run the Streamlit app (entrypoint = Home page)
CMD ["streamlit", "run", "ui/Home.py", "--server.port=8501", "--server.enableCORS=false"]
