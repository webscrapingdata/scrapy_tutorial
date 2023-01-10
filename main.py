
from scrapy.selector import Selector
body = '<html><body><span>good</span></body></html>'
print(Selector(text=body).xpath('//span/text()').get())
# Using CSS
print(Selector(text=body).css('span::text').get())