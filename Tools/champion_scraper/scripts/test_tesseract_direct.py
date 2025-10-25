"""
Direct test of pytesseract configuration
"""
import os
import platform

try:
    import pytesseract
    print("✓ pytesseract imported successfully")
    
    # Configure tesseract path for Windows
    if platform.system() == 'Windows':
        possible_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        ]
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✓ Found Tesseract at: {path}")
                pytesseract.pytesseract.tesseract_cmd = path
                break
    
    # Test if tesseract is accessible
    version = pytesseract.get_tesseract_version()
    print(f"✓ Tesseract version: {version}")
    print(f"✓ Tesseract command: {pytesseract.pytesseract.tesseract_cmd}")
    
    # Try a simple OCR test
    from PIL import Image
    import requests
    from io import BytesIO
    
    print("\nTesting OCR on champion image...")
    url = "https://ayumilove.net/files/games/raid_shadow_legends/champion/Gretel_Hagbane.jpg"
    response = requests.get(url, timeout=10)
    img = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    print(f"✓ OCR completed, extracted {len(text)} characters")
    print("\nFirst 500 characters of OCR output:")
    print(text[:500])
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
