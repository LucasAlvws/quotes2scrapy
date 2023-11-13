import scrapy


class Quotes2scrapeSpider(scrapy.Spider):
    name = "quotes2scrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

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
