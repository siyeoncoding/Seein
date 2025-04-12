from PIL import Image
import pytesseract
import os

# 윈도우에 설치된 Tesseract 경로 지정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str, lang: str = "kor+eng") -> str:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=lang)
        return text.strip()
    except Exception as e:
        return f"OCR 실패: {str(e)}"
