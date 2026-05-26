import feedparser
import time
import requests

from datetime import datetime
from summarizer import summarize
from article_reader import get_article_text
from telegram_sender import send_message

rss_feeds = [
    ("TechCrunch", "https://techcrunch.com/feed/", True),
    ("The Verge", "https://www.theverge.com/rss/index.xml", True),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/", True)
]

today = datetime.now().strftime("%Y-%m-%d")

filename = f"reports/{today}-news.txt"

all_articles = []

with open(filename, "w", encoding="utf-8") as file:

    file.write("오늘의 IT 뉴스\n\n")

    for site_name, rss_url, use_scraping in rss_feeds:

        #확인
        print(site_name)
        
        response = requests.get(
            rss_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )   

        feed = feedparser.parse(response.content)

        #확인
        print(len(feed.entries))

        if feed.entries:
            all_articles.append(
               f"\n\n========== {site_name} ==========\n\n"
            )   

        for i, entry in enumerate(feed.entries[:20], start=1):

            news = f"[기사 {i}] {entry.title}\n"
            link = f"{entry.link}\n"

            if use_scraping:
                article_text = get_article_text(entry.link)
            else:
                article_text = entry.summary

            if not article_text:
                article_text = entry.summary

            article_data = (
                f"[언론사] {site_name}\n" +
                news +
                link +
                article_text +
                "\n\n========== 기사 끝 ==========\n\n"
            )

            all_articles.append(article_data)

    # 기사 전체 합치기
    all_text = "\n".join(all_articles)

    # Gemini 1회 호출
    summary = summarize(all_text)

    # 출력
    print(summary)

    # 파일 저장
    file.write(summary)

    # Telegram 전송
    send_message(summary)

print(f"\n저장 완료: {filename}")
