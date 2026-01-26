#!/usr/bin/env python3
"""
Image to WebP Converter
Converts all images in a directory to WebP format for better web performance.

Usage:
    python convert_to_webp.py [source_directory] [output_directory]
    
If no directories specified, converts images in current directory.
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Installing...")
    os.system("pip3 install Pillow --break-system-packages")
    from PIL import Image

# Supported input formats
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif'}

def convert_to_webp(input_path, output_path, quality=85):
    """Convert a single image to WebP format."""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (for PNG with transparency, use RGBA)
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # Keep transparency
                img.save(output_path, 'WEBP', quality=quality, lossless=False)
            else:
                # Convert to RGB for JPG etc
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(output_path, 'WEBP', quality=quality)
        return True
    except Exception as e:
        print(f"  Error converting {input_path}: {e}")
        return False

def process_directory(source_dir, output_dir=None):
    """Process all images in a directory."""
    source_path = Path(source_dir)
    
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = source_path
    
    converted = 0
    failed = 0
    skipped = 0
    
    print(f"\n🖼️  Image to WebP Converter")
    print(f"{'='*50}")
    print(f"Source: {source_path}")
    print(f"Output: {output_path}")
    print(f"{'='*50}\n")
    
    # Find all image files
    image_files = []
    for ext in SUPPORTED_FORMATS:
        image_files.extend(source_path.glob(f'*{ext}'))
        image_files.extend(source_path.glob(f'*{ext.upper()}'))
    
    if not image_files:
        print("No supported images found.")
        print(f"Supported formats: {', '.join(SUPPORTED_FORMATS)}")
        return
    
    print(f"Found {len(image_files)} image(s) to convert:\n")
    
    for img_file in sorted(image_files):
        # Skip if already WebP
        if img_file.suffix.lower() == '.webp':
            skipped += 1
            continue
        
        # Create output filename
        output_file = output_path / f"{img_file.stem}.webp"
        
        # Check if output already exists
        if output_file.exists():
            print(f"  ⏭️  {img_file.name} → already exists, skipping")
            skipped += 1
            continue
        
        # Convert
        print(f"  Converting: {img_file.name}", end="")
        
        if convert_to_webp(img_file, output_file):
            # Show size comparison
            original_size = img_file.stat().st_size / 1024
            new_size = output_file.stat().st_size / 1024
            savings = ((original_size - new_size) / original_size) * 100
            
            print(f" → {output_file.name}")
            print(f"     {original_size:.1f}KB → {new_size:.1f}KB ({savings:.1f}% smaller)")
            converted += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Converted: {converted}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"❌ Failed: {failed}")
    print(f"{'='*50}\n")

def main():
    if len(sys.argv) >= 2:
        source_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) >= 3 else None
    else:
        # Default to assets/images in the portfolio
        source_dir = os.path.dirname(os.path.abspath(__file__))
        source_dir = os.path.join(source_dir, 'assets', 'images')
        output_dir = None
    
    if not os.path.exists(source_dir):
        print(f"Directory not found: {source_dir}")
        sys.exit(1)
    
    process_directory(source_dir, output_dir)

if __name__ == "__main__":
    main()
