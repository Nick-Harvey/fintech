# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_newline(value):
	return value.replace('\n\t\t', '').strip()


class PachScreenerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class morningstarNews(scrapy.Item):

	# articles dictionary containing article title and url
	article = scrapy.Field()

	# Headline Title
	headline_str = scrapy.Field(
		input_processor=MapCompose(remove_newline),
		output_processor=TakeFirst()
		)

	# Headline URL
	url = scrapy.Field()
