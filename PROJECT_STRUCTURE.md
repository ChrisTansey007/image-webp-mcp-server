# Project Structure Summary

## Image-to-WebP MCP Server

This repository contains a complete FastMCP server for converting images to WebP format.

### 📁 Project Structure
```
image-webp-mcp-server/
├── image_webp_mcp_server.py    # Main server implementation
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker container configuration
├── docker-compose.yml          # Docker Compose for easy deployment
├── README.md                   # Comprehensive documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── test_server.py              # Test suite for the server
├── setup_git.sh               # Bash script to initialize git
├── setup_git.ps1              # PowerShell script to initialize git
└── PROJECT_STRUCTURE.md       # This file
```

### 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install fastmcp pillow
   ```

2. **Run the Server:**
   ```bash
   python image_webp_mcp_server.py
   ```

3. **Test the Server:**
   ```bash
   python test_server.py
   ```

### 🐳 Docker Deployment

1. **Build and Run:**
   ```bash
   docker-compose up --build
   ```

2. **Or manually:**
   ```bash
   docker build -t image-webp-mcp-server .
   docker run -p 8000:8000 image-webp-mcp-server
   ```

### 🔧 Tools Available

- **convert_image**: Convert single image to WebP
- **bulk_convert**: Convert multiple images to WebP

Both tools support:
- Quality adjustment (0-100)
- Optional resizing with aspect ratio preservation
- Error handling and reporting

### 📊 Server Endpoint

The server runs on: `http://localhost:8000/mcp`

### 🧪 Testing

Run the included test suite to verify functionality:
```bash
python test_server.py
```

### 📝 License

MIT License - see LICENSE file for details.
