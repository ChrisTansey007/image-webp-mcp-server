@echo off
cd /d "C:\Users\theca\Desktop\image-webp-mcp-server"
echo Cleaning up project - removing temporary setup files...
echo.
echo Current clean project structure:
dir /b
echo.
echo Adding changes to git...
git add .
echo.
echo Committing cleanup...
git commit -m "Clean up project structure - remove temporary setup files

- Removed development/setup helper scripts
- Updated PROJECT_STRUCTURE.md to reflect clean structure
- Repository now contains only essential project files"
echo.
echo Pushing cleanup to GitHub...
git push
echo.
echo Project cleanup complete!
echo Repository now contains only essential files.
pause
