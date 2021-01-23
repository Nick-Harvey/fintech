# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import logging

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

logger = logging.getLogger()

class PachScreenerNewsPipeline:
	"""Pipeline to output ticker news links"""

	def open_spider(self, spider):
		self.file = open('news.json', 'w+')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):

		news = ItemAdapter(item)

		line = json.dumps((news['headline_str'], news['url'])) + "\n"
		self.file.write(line)
		return item

class PachScreenerPipeline:
    def process_item(self, item, spider):
        return item
