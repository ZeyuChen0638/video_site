import base64
import os

def encode_base64(img_path):
    with open(img_path, 'rb') as img:
        content = img.read()
        base64_data = base64.b64encode(content)
        base64_str = str(base64_data, 'utf-8')
        return 'data:image/jpeg;base64,' + base64_str