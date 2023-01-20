import scrapy
from langdetect import detect

from ..utils.dash_remover import clean
from ..utils.noise_word_remover import remove
from ..utils.highlights_remover import remove_highlights


class KamiSpider(scrapy.Spider):
    name = 'kami'
    start_urls = ['file:///Users/jamesesguerra/thesis/kami.html']


    def __init__(self, **kwargs):
        super().__init__(**kwargs) 


    def parse(self, response):
        articles = response.css('div.c-article-card-horizontal__container a::attr(href)').getall()

        for article in articles:
            yield response.follow(article, callback=self.parse_articles)


    def parse_articles(self, response):
        # for article text
        bold_text = remove(response.css("strong::text").getall())
        article_text = remove(response.css("div.post__content p *::text").getall())

        cleaned_article_text = remove_highlights(bold_text, article_text)
        article_text = ' '.join(cleaned_article_text).strip()

        # for summary
        highlights = list(filter(lambda x: x.startswith("-"), response.css('strong::text').getall()))
        cleaned_highlights = list(map(clean, highlights))
        summary = '.'.join(cleaned_highlights).strip()


        if detect(summary) != "en":
            yield {
                'title': response.css("h1.c-main-headline::text").get(),
                'article_text': article_text,
                'summary': summary,
                'article_date': response.css("time::text").get(),
                'source': response.request.url
            }