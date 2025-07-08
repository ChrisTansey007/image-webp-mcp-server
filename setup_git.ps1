# PowerShell setup script for initializing the git repository

# Navigate to the script directory
Set-Location $PSScriptRoot

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

Write-Host "Git repository initialized successfully!" -ForegroundColor Green
Write-Host "Repository is ready to be pushed to GitHub." -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a new repository on GitHub" -ForegroundColor White
Write-Host "2. Add the remote: git remote add origin <your-repo-url>" -ForegroundColor White
Write-Host "3. Push the code: git push -u origin main" -ForegroundColor White
