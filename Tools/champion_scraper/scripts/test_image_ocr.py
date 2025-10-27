"""Quick test to see what's in the HellHades Geomancer image"""
from PIL import Image
import pytesseract
import os

# Configure tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Test the Geomancer image
image_path = r'c:\GIT\Raid_Tools\input\Stat_Test\Geomancer.jpg'

if os.path.exists(image_path):
    img = Image.open(image_path)
    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
    print(f"\nExtracting text...\n")
    
    text = pytesseract.image_to_string(img)
    print("="*80)
    print("EXTRACTED TEXT:")
    print("="*80)
    print(text)
    print("="*80)
else:
    print(f"Image not found: {image_path}")
