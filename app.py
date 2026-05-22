import feedparser
import time

from datetime import datetime
from summarizer import summarize
from article_reader import get_article_text
from telegram_sender import send_message

rss_url = "https://techcrunch.com/feed/"

feed = feedparser.parse(rss_url)

today = datetime.now().strftime("%Y-%m-%d")

filename = f"reports/{today}-news.txt"

with open(filename, "w", encoding="utf-8") as file:

    file.write("오늘의 IT 뉴스\n\n")

    for i, entry in enumerate(feed.entries[:3], start=1):

        news = f"{i}. {entry.title}\n"
        link = f"링크: {entry.link}\n"

        article_text = get_article_text(entry.link)
        
        summary = summarize(article_text) + "\n"

        line = "-" * 50 + "\n"

        print(news)
        print(link)
        print(summary)

        file.write(news)
        file.write(link)
        file.write(summary)
        file.write(line)

        send_message(news + "\n" + link + "\n" + summary)

        time.sleep(5)

print(f"\n저장 완료: {filename}")
