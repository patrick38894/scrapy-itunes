import scrapy
import urllib2

from musicdb.items import *

class ItunesSpider(scrapy.Spider):
	download_delay = 0.25
	name = "itunes"
	allowed_domains = ["itunes.apple.com"]
	start_urls = ["https://itunes.apple.com/us/genre/music/id34"]

	def parse(self, response):
		"""parse all genres"""
		for sel in response.xpath("//body/div/div/div/div[contains(@id,'genre-nav')]/div/ul/li/ul/li/a"):
			genre = sel.xpath('text()').extract()[0]
			url = sel.xpath('@href').extract()[0]
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
			yield request

	def parse_artist(self, response):
		genre = response.meta['genre']
		artist = response.meta['artist']


		####################3
                n = 0
                for sel in response.xpath("//body/div/div/div/div/div/div/div/table/tbody/tr[contains(@class,'song music')]"):
                        entry = Top10Item()
                        entry['artist'] = str(artist)
                        entry['track_name'] = str(sel.xpath('td/span/a/span/text()').extract()[0])
                        entry['jsontype'] = 'top10'
                        if (n >= 10):
                                break
                        n = n + 1
                        yield entry
		#######################

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
		album_price = response.xpath("//body/div/div/div/div/div/ul/li/span[contains(@class,'price')]/text()").extract()[0]
		release_date  = response.xpath("//body/div/div/div/div/div/ul/li[contains(@class,'release-date')]/span[contains(@itemprop,'dateCreated')]/text()").extract()[0]

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
			entry['release_date'] = str(release_date)
			entry['album_price'] = str(album_price)
			entry['jsontype'] = 'general'


			yield entry

