#!/usr/bin/env python3
"""
Simple test script for the Image-to-WebP MCP Server
"""
import requests
import json
import tempfile
import os
from PIL import Image

# Server configuration
SERVER_URL = "http://localhost:8000/mcp"

def create_test_image(filename: str, size: tuple = (200, 200), color: str = "red"):
    """Create a simple test image"""
    img = Image.new('RGB', size, color=color)
    img.save(filename, 'PNG')
    return filename

def test_single_conversion():
    """Test single image conversion"""
    print("Testing single image conversion...")
    
    # Create a test image
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        test_image = create_test_image(tmp.name, (300, 200), "blue")
    
    try:
        # Test the convert_image tool
        payload = {
            "tool": "convert_image",
            "arguments": {
                "image_path": test_image,
                "quality": 85,
                "width": 150
            }
        }
        
        response = requests.post(SERVER_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Single conversion successful: {result}")
            
            # Check if output file exists
            if os.path.exists(result.get('output', '')):
                print(f"✅ Output file created: {result['output']}")
            else:
                print("❌ Output file not found")
        else:
            print(f"❌ Single conversion failed: {response.status_code} - {response.text}")
    
    finally:
        # Cleanup
        if os.path.exists(test_image):
            os.unlink(test_image)

def test_bulk_conversion():
    """Test bulk image conversion"""
    print("\nTesting bulk image conversion...")
    
    # Create multiple test images
    test_images = []
    colors = ["red", "green", "blue"]
    
    for i, color in enumerate(colors):
        with tempfile.NamedTemporaryFile(suffix=f'_test_{i}.png', delete=False) as tmp:
            test_image = create_test_image(tmp.name, (200, 200), color)
            test_images.append(test_image)
    
    try:
        # Test the bulk_convert tool
        payload = {
            "tool": "bulk_convert",
            "arguments": {
                "image_paths": test_images,
                "quality": 80,
                "width": 100,
                "height": 100
            }
        }
        
        response = requests.post(SERVER_URL, json=payload)
        
        if response.status_code == 200:
            results = response.json()
            print(f"✅ Bulk conversion successful: {len(results)} images processed")
            
            for result in results:
                if 'error' in result:
                    print(f"❌ Error processing {result['input']}: {result['error']}")
                else:
                    print(f"✅ Converted: {result['input']} -> {result['output']}")
        else:
            print(f"❌ Bulk conversion failed: {response.status_code} - {response.text}")
    
    finally:
        # Cleanup
        for test_image in test_images:
            if os.path.exists(test_image):
                os.unlink(test_image)

def test_server_health():
    """Test if server is running"""
    print("Testing server health...")
    
    try:
        response = requests.get(SERVER_URL.replace('/mcp', '/health'))
        if response.status_code == 200:
            print("✅ Server is healthy")
            return True
        else:
            print(f"⚠️  Server health check returned: {response.status_code}")
            return True  # Server might not have health endpoint, continue with tests
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running on http://localhost:8000")
        return False

if __name__ == "__main__":
    print("Image-to-WebP MCP Server Test Suite")
    print("="*50)
    
    if test_server_health():
        test_single_conversion()
        test_bulk_conversion()
        print("\n✅ Test suite completed!")
    else:
        print("\n❌ Cannot run tests - server is not accessible")
        print("Start the server with: python image_webp_mcp_server.py")
