@echo off
cd /d "C:\Users\theca\Desktop\image-webp-mcp-server"
echo Initializing Git repository...
git init
echo Adding files...
git add .
echo Creating initial commit...
git commit -m "Initial commit: Image-to-WebP MCP Server - FastMCP server for converting images to WebP format - Support for single and bulk image conversion - Optional resizing with aspect ratio preservation - Docker support and comprehensive documentation"
echo.
echo Git repository initialized successfully!
echo.
echo Repository is ready for GitHub.
echo Next step: Create repository on GitHub and push.
pause
