import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize(text):

    prompt = f"""
다음 뉴스들 중에서 가장 중요한 IT 뉴스 5개만 선택해서 한국어로 매우 짧고 간결하게 요약해줘.

조건:
- 반드시 언론사별로 묶어서 정리
- 같은 언론사의 뉴스는 한 섹션 아래에 모아서 출력
- 언론사 섹션을 여러 번 반복하지 말 것
- 뉴스 중요도보다 언론사 그룹 유지가 우선
- AI, 빅테크, 스타트업, 보안, 클라우드, 반도체 우선
- 단순 제품 홍보성 뉴스는 우선순위 낮게 처리
- 단, 산업적으로 중요한 제품 발표는 포함 가능
- 작성자 소개 문구 제외

형식:
### 언론사명

#### 제목
- 핵심 요약 1줄
- 중요키워드 2-3개

뉴스 목록 :
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text
