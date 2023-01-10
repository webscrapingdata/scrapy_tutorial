import scrapy

# Import Response class from scrapy.http module
from scrapy.http import Response

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['https://asaxiy.uz/uz/product/brand/apple/page=2','http://python.org/']

    def parse(self, response: Response):
        print('Hello World!')
        print(response)
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        data=response.css('div.card') # Selector  List
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
