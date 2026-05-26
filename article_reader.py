from newspaper import Article

def get_article_text(url):

    try:
        article = Article(url)

        article.download()
        article.parse()

        return article.text[:500]

    except Exception as e:
        print(f"기사 읽기 실패: {url}")
        print(e)

        return ""
