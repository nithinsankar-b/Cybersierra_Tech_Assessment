import base64
from PIL import Image
from io import BytesIO

def base64_to_image(base64_string):
    """Convert base64 string to PIL Image"""
    byte_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(byte_data))