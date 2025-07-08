FROM python:3.11-slim

# Install dependencies
RUN pip install --no-cache-dir fastmcp pillow

# Copy server
COPY image_webp_mcp_server.py /app/server.py

WORKDIR /app

# Expose the HTTP port
EXPOSE 8000

# Start FastMCP server
CMD ["python", "server.py"]
