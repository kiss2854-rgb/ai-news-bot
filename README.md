# AI News Bot

매일 주요 IT / AI 뉴스를 수집하고
Gemini를 통해 한국어로 요약 후 텔레그램으로 자동 전송하는 뉴스 봇입니다.

---

## 소개

최신 IT 뉴스를 수집하고 Gemini를 통해 한국어로 요약한 뒤
텔레그램으로 자동 전송합니다.

---

## 기능

* 뉴스 수집 (TechCrunch / The Verge / VentureBeat)
* Gemini 기반 한국어 요약
* 텔레그램 자동 전송
* cron 스케줄링 지원
* TXT 리포트 저장
* 텔레그램 친화 UI 포맷

---

## 설치 방법

```bash
git clone https://github.com/YOUR_ID/ai-news-bot.git
cd ai-news-bot

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 환경 변수

`.env`

```env
GEMINI_API_KEY=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

---

## 실행

```bash
python app.py
```

---

## cron 예시

매일 오전 7시 실행:

```cron
0 7 * * * root cd /root/ai-news-bot && /root/ai-news-bot/venv/bin/python app.py >> cron.log 2>&1
```

---

## 디렉토리 구조

```text
ai-news-bot/
├── app.py
├── requirements.txt
├── reports/
├── cron.log
└── README.md
```
