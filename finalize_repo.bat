@echo off
cd /d "C:\Users\theca\Desktop\image-webp-mcp-server"
echo Adding new files...
git add .
echo Creating commit...
git commit -m "Add GitHub repository creation helper scripts"
echo.
echo Repository is ready for GitHub!
echo.
echo Final project structure:
dir /b
