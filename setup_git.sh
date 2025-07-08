#!/bin/bash
# Setup script for initializing the git repository

# Navigate to the project directory
cd "$(dirname "$0")"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Image-to-WebP MCP Server

- FastMCP server for converting images to WebP format
- Support for single and bulk image conversion
- Optional resizing with aspect ratio preservation
- Docker support with Dockerfile and docker-compose
- Comprehensive documentation and test suite"

echo "Git repository initialized successfully!"
echo "Repository is ready to be pushed to GitHub."
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote: git remote add origin <your-repo-url>"
echo "3. Push the code: git push -u origin main"
