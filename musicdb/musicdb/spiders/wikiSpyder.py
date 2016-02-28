import scrapy

from musicdb.items import *

class WikiSpyder(scrapy.Spider):
	name = "wikiSpyder"
	allowed_domains = ["wikipedia.org"]
	start_urls = ["https://en.wikipedia.org/wiki/List_of_roots_rock_bands_and_musicians"]

	def parse(self, response):
		for sel in response.xpath("//body/div/div/div[contains(@id,'mw-content-text')]/div/ul/li"):
			item = Artist()
			item['name'] = sel.xpath('a/text()').extract()
			print item['name']
			yield item
