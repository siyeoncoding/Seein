from fastapi import APIRouter, File, UploadFile, HTTPException
from PIL import Image
import pytesseract
import io


router = APIRouter()

# ✨ Tesseract 실행 경로 지정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@router.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image, lang='kor+eng')
        return {"text": text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summary")
async def summarize_from_image(file: UploadFile = File(...)):
    try:
        summarizer = Pororo(task="summary", lang="ko")

        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        text = pytesseract.image_to_string(image, lang="kor+eng")

        if not text.strip():
            raise HTTPException(status_code=400, detail="텍스트가 인식되지 않았습니다.")

        summary = summarizer(text)

        return {
            "original_text": text.strip(),
            "summary": summary.strip()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"처리 중 오류 발생: {str(e)}")
