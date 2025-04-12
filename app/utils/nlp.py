from pororo import Pororo

# 요약기 불러오기 (최초 실행 시 모델 다운로드)
summarizer = Pororo(task="summary", lang="ko")

def summarize_text(text: str) -> str:
    try:
        return summarizer(text)
    except Exception as e:
        return f"요약 실패: {str(e)}"
