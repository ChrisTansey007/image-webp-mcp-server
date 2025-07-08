@echo off
cd /d "C:\Users\theca\Desktop\image-webp-mcp-server"
echo Checking Git status...
git status
echo.
echo Repository Information:
echo =====================
echo Repository name: image-webp-mcp-server
echo Description: FastMCP server for converting images to WebP format with optional resizing
echo.
echo To create GitHub repository:
echo 1. Go to: https://github.com/new
echo 2. Repository name: image-webp-mcp-server
echo 3. Description: FastMCP server for converting images to WebP format with optional resizing
echo 4. Choose Public or Private
echo 5. Do NOT initialize with README (we already have one)
echo 6. Click "Create repository"
echo.
echo After creating the repository, run these commands:
echo git remote add origin https://github.com/[YourUsername]/image-webp-mcp-server.git
echo git branch -M main
echo git push -u origin main
echo.
pause
