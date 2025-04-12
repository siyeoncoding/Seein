import requests

import cv2
import numpy as np
from PIL import Image
import pytesseract




def preprocess_image(image_path: str) -> Image.Image:
    # OpenCV로 이미지 로드 (grayscale)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 이진화 (adaptive thresholding)
    img = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # 노이즈 제거 (morphological operations)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # 다시 PIL 이미지로 변환
    pil_img = Image.fromarray(img)
    return pil_img




#url = "http://127.0.0.1:8020/api/summary"
def summarize_image_from_server(image_path: str) -> dict:
    # OCR 전처리
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image, lang='kor+eng')

    if not text.strip():
        return {"original_text": "", "summary": "텍스트를 인식하지 못했습니다."}

    # 요약 서버에 요청
    url = "http://192.168.0.5:8020/api/summary"  # ✅ PC의 IP로 수정
    with open(image_path, "rb") as image_file:
        files = {"file": image_file}
        response = requests.post(url, files=files)

    if response.status_code != 200:
        raise Exception(f"요약 서버 오류: {response.status_code} - {response.text}")

    return {
        "original_text": text.strip(),
        "summary": response.json().get("summary", "")
    }
