# Use an official Python runtime
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "ui/main.py", "--server.port=8501", "--server.enableCORS=false"]
