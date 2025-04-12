import requests

SUMMARY_API_URL = "http://localhost:8020/api/v1/summary"

def request_summary(image_path: str) -> dict:
    """
    로컬 Pororo 요약 서버에 이미지 파일을 전송하고 요약 결과를 받아온다.
    :param image_path: 요약할 이미지 파일의 경로
    :return: {"original_text": ..., "summary": ...}
    """
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(SUMMARY_API_URL, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"요약 실패: {response.status_code}, {response.text}")
