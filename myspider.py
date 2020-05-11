import scrapy
old_url ='https://blog.scrapinghub.com'
class WebSpider(scrapy.Spider):
    name = 'webspider'
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes']

    def parse(self, response):
        for title in response.xpath("//a"):
            yield{'href':title.xpath("//a/@href").extract_first()
            }
        
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)