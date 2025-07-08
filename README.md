# Image-to-WebP MCP Server

A FastMCP server that provides image conversion tools to convert images to WebP format with optional resizing capabilities.

## Features

- **Single Image Conversion**: Convert one image to WebP format
- **Bulk Image Conversion**: Convert multiple images in a single request
- **Optional Resizing**: Resize images while maintaining aspect ratio
- **Quality Control**: Adjustable WebP quality settings
- **HTTP Transport**: Accessible via HTTP for easy integration

## Tools

### 1. `convert_image`
Convert a single image to WebP format with optional resizing.

**Parameters:**
- `image_path` (str): Path to the input image
- `quality` (int, default=80): WebP quality (0-100)
- `width` (Optional[int]): Target width (maintains aspect ratio if height not specified)
- `height` (Optional[int]): Target height (maintains aspect ratio if width not specified)

**Returns:** Dictionary with conversion details

### 2. `bulk_convert`
Convert multiple images to WebP format in a single request.

**Parameters:**
- `image_paths` (List[str]): List of paths to input images
- `quality` (int, default=80): WebP quality (0-100)
- `width` (Optional[int]): Target width for all images
- `height` (Optional[int]): Target height for all images

**Returns:** List of dictionaries with conversion details for each image

## Installation

### Prerequisites
- Python 3.11+
- pip or uv package manager

### Install Dependencies

Using pip:
```bash
pip install fastmcp pillow
```

Using uv:
```bash
uv pip install fastmcp pillow
```

## Usage

### Running the Server

#### Local Development
```bash
python image_webp_mcp_server.py
```

The server will start on `http://0.0.0.0:8000/mcp`

#### Using Docker

1. Build the Docker image:
```bash
docker build -t image-webp-mcp-server .
```

2. Run the container:
```bash
docker run -p 8000:8000 -v /path/to/your/images:/images image-webp-mcp-server
```

### Example Usage

Once the server is running, you can use any MCP-compatible client to access the tools:

#### Convert Single Image
```json
{
  "tool": "convert_image",
  "arguments": {
    "image_path": "/path/to/image.jpg",
    "quality": 85,
    "width": 800
  }
}
```

#### Bulk Convert Images
```json
{
  "tool": "bulk_convert",
  "arguments": {
    "image_paths": [
      "/path/to/image1.jpg",
      "/path/to/image2.png",
      "/path/to/image3.gif"
    ],
    "quality": 80,
    "width": 1200,
    "height": 800
  }
}
```

## Supported Image Formats

The server supports all image formats that PIL (Python Imaging Library) can handle:
- JPEG
- PNG
- GIF
- BMP
- TIFF
- And many more

## Configuration

### Quality Settings
- **0-100**: WebP quality level
- **80**: Default quality (good balance of size and quality)
- **Higher values**: Better quality, larger file size
- **Lower values**: Smaller file size, reduced quality

### Resizing Behavior
- If both `width` and `height` are specified: Image is resized to exact dimensions
- If only `width` is specified: Height is calculated to maintain aspect ratio
- If only `height` is specified: Width is calculated to maintain aspect ratio
- If neither is specified: Original dimensions are preserved

## Error Handling

The server gracefully handles errors during conversion:
- Invalid file paths
- Unsupported image formats
- File permission issues
- Memory limitations

Errors are returned in the response with descriptive messages.

## Development

### Project Structure
```
image-webp-mcp-server/
├── image_webp_mcp_server.py  # Main server file
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Image processing powered by [Pillow](https://pillow.readthedocs.io/)
