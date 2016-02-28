import scrapy
import urllib2

from musicdb.items import *

class ItunesSpider(scrapy.Spider):
	download_delay = 1.0
	name = "itunes"
	allowed_domains = ["itunes.apple.com"]
	start_urls = ["https://itunes.apple.com/us/genre/music/id34"]

	def parse(self, response):
		"""parse all genres"""
		for sel in response.xpath("//body/div/div/div/div[contains(@id,'genre-nav')]/div/ul/li/ul/li/a"):
			genre = sel.xpath('text()').extract()[0]
			url = sel.xpath('@href').extract()[0]
			#print (url)
			request = scrapy.Request(url, callback=self.parse_genre)
			request.meta['genre'] = genre
			yield request

	def parse_genre(self, response):
		genre = response.meta['genre']
		for sel in response.xpath("//body/div/div/div/div[contains(@id,'selectedgenre')]/div/div/ul/li/a"):
			url = sel.xpath('@href').extract()[0]
			artist = sel.xpath('text()').extract()[0]
			request = scrapy.Request(url, callback=self.parse_artist)		
			request.meta['genre'] = genre
			request.meta['artist'] = artist
			#print (artist)
			yield request

	def parse_artist(self, response):
		genre = response.meta['genre']
		artist = response.meta['artist']
		for sel in response.xpath("//body/div/div/div/div/div/div/div/div/div/div/ul/li/a[contains(@class, 'name')]"):
			url = sel.xpath('@href').extract()[0]
			album = sel.xpath('span/text()').extract()[0]
			request = scrapy.Request(url, callback=self.parse_album)		
			request.meta['genre'] = genre
			request.meta['artist'] = artist
			request.meta['album'] = album
			yield request

	def parse_album(self, response):
		genre = response.meta['genre']
		artist = response.meta['artist']
		album = response.meta['album']
		for sel in response.xpath("//body/div/div/div/div/div/div/table/tbody/tr"):
			tracknum = sel.xpath('td/span/span/text()').extract()[0]
			song = sel.xpath('td/span/span/text()').extract()[1]
			time = sel.xpath('td/span/span/text()').extract()[2]
			price = sel.xpath('td/span/span/text()').extract()[3]
		
			entry = MusicdbItem()
			entry['genre']= str(genre)
			entry['artist_name'] = str(artist)
        		entry['track_name'] = str(song)
			entry['song_length'] = str(time)
			entry['song_price'] = str(price)
			entry['track_number'] = str(tracknum)
			entry['album'] = str(album)


			yield entry

