# image_webp_mcp_server.py
"""
FastMCP server: Image-to-WebP (with optional resize)
---------------------------------------------------
Tools:
1. convert_image(...) – convert ONE image (optionally resize & set quality)
2. bulk_convert(...)  – convert MANY images in one request

Run locally (HTTP transport):
    uv pip install fastmcp pillow        # or pip install …
    python image_webp_mcp_server.py

The server will start on http://0.0.0.0:8000/mcp
"""
import os
from typing import List, Optional, Tuple, Dict
from fastmcp import FastMCP
from PIL import Image


# -----------------------------------------------------------------------------
# Helper functions (unchanged from your CLI script, just moved into a module)
# -----------------------------------------------------------------------------

def calculate_new_size(
    orig_w: int,
    orig_h: int,
    tgt_w: Optional[int],
    tgt_h: Optional[int],
) -> Tuple[int, int]:
    """Compute the new size while preserving aspect ratio when one dimension is missing."""
    if tgt_w and tgt_h:
        return tgt_w, tgt_h
    if tgt_w:
        new_h = round(orig_h * (tgt_w / orig_w))
        return tgt_w, new_h
    if tgt_h:
        new_w = round(orig_w * (tgt_h / orig_h))
        return new_w, tgt_h
    return orig_w, orig_h


def convert_to_webp(
    image_path: str,
    *,
    quality: int = 80,
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> Dict[str, str]:
    """Core converter used by both MCP tools."""
    file_name, _ = os.path.splitext(image_path)
    output_path = f"{file_name}.webp"
    
    with Image.open(image_path) as img:
        # resize if user requested
        if width or height:
            new_size = calculate_new_size(img.width, img.height, width, height)
            img = img.resize(new_size, Image.LANCZOS)
        img.save(output_path, "webp", quality=quality, method=6)
    
    return {
        "input": image_path,
        "output": output_path,
        "quality": quality,
        "width": width or "orig",
        "height": height or "orig",
    }


# -----------------------------------------------------------------------------
# FastMCP server + tools
# -----------------------------------------------------------------------------

mcp = FastMCP("ImageWebPConverter")


@mcp.tool
def convert_image(
    image_path: str,
    quality: int = 80,
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> Dict[str, str]:
    """
    Convert ONE image to WebP; optionally resize.
    Returns a small JSON payload describing the result.
    """
    return convert_to_webp(
        image_path, quality=quality, width=width, height=height
    )


@mcp.tool
def bulk_convert(
    image_paths: List[str],
    quality: int = 80,
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> List[Dict[str, str]]:
    """
    Convert MANY images in a single call.
    The list preserves the order of `image_paths`.
    """
    results = []
    for path in image_paths:
        try:
            results.append(
                convert_to_webp(
                    path, quality=quality, width=width, height=height
                )
            )
        except Exception as exc:
            results.append({"input": path, "error": str(exc)})
    return results


if __name__ == "__main__":
    # Expose over HTTP so any MCP-compatible client (or FastAPI) can hit /mcp
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")
