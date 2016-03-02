# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Top10Item(scrapy.Item):
	jsontype = scrapy.Field()
	artist = scrapy.Field()
	track_name = scrapy.Field()
	

class MusicdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	artist_name = scrapy.Field()
	track_name = scrapy.Field()
	song_length = scrapy.Field()
	song_price = scrapy.Field()
	track_number = scrapy.Field()
	album = scrapy.Field()
	genre = scrapy.Field()
	jsontype = scrapy.Field()

