from newspaper import Article

def get_article_text(url):

    article = Article(url)

    article.download()
    article.parse()

    return article.text[:500]
