import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize(text):

    prompt = f"""
다음 뉴스들을 언론사별로 정리해서 한국어로 요약해줘.

조건:
- 각 언론사 섹션에서 최대 2개 기사 선택
- 기사 개수를 임의로 줄이지 말 것
- 기사의 언론사를 절대 변경하지 말 것
- 각 기사 사이에는 빈 줄 1개 추가
- 같은 언론사의 뉴스는 한 섹션 아래에 모아서 출력
- 모든 언론사 섹션은 동일한 형식과 이모지를 사용
- 뉴스 중요도보다 언론사 그룹 유지가 우선
- AI, 빅테크, 스타트업, 보안, 클라우드, 반도체 우선
- 단순 제품 홍보성 뉴스 제외
- 산업적으로 중요한 제품 발표는 포함 가능
- 기사 제목은 자연스러운 한국어 제목으로 번역
- 제목은 20자 이하로 뉴스 헤드라인 스타일로 짧고 직관적으로 작성
- 제목과 본문에는 불필요한 특수문자(*, _, [, ]) 사용 금지
- 작성자 소개 문구 제외
- 반드시 기사 링크 포함
- 키워드는 2-3개
- 키워드는 자연스러운 한글 띄어쓰기 사용
- 키워드와 링크는 공백 2칸 들여쓰기
- 동일 주제 뉴스는 하나만 선택
- 중복 기사 제거
- 링크는 반드시 클릭 가능한 형태로 출력. 형식: 🔗 [기사보기](실제URL)

출력형식:
📰 오늘의 IT 뉴스

이모지+언론사명
• 제목
  - 핵심 요약
  🏷️ 키워드
  🔗 링크

뉴스 목록 :
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
