import scrapy

class ImageSpider(scrapy.Spider):
  name = "image_spider"
  allowed_domains = ["example.com"]
  start_urls = ['https://en.wikipedia.org/wiki/Udaipur']

  def parse(self, response):
    image_urls = response.xpath("//img/@src").extract()
    city_data = {
        "image_url": image_urls
    }
    yield city_data
