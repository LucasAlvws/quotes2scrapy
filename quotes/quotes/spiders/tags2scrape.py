import scrapy


class Tags2scrapeSpider(scrapy.Spider):
    name = "tags2scrape"
    allowed_domains = ["quotes.toscrape.com"]
    #start_urls = ["https://quotes.toscrape.com"]
    def __init__(self, tag = None, *args ,**kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f"https://quotes.toscrape.com/tag/{tag}/page/1/"]

    def parse(self, response):
        for filmes in response.css('.quote'):
            yield{
                'quote' : filmes.css('.text::text').get(),
                'author' : filmes.css('.author::text').get(),
                'tags' : filmes.css('.tags .tag::text').getall()
            }
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url="https://quotes.toscrape.com" + next_page, callback=self.parse)
        pass
