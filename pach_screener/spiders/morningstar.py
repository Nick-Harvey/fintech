import scrapy
import os
import csv
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from scrapy.loader import ItemLoader
from pach_screener.items import morningstarNews


# Set the path for the selenium web-driver
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'), options=chrome_options)

#Pachyderm Settings
input_dir = os.getenv('INPUT_DIR')

class MorningStarSpider(scrapy.Spider):
	name = 'morningstar'
	allowed_domains = ['morningstar.com/']
	start_urls = ['https://www.morningstar.com/']
	
	def start_requests(self):
		# Iterate through each ticker symbol and scrape data from finviz.
		with open('dev_test.csv') as f:
			f_csv = csv.reader(f)

			for row in f_csv:
				current_ticker = row[2]
				try:
					url = 'https://www.morningstar.com/stocks/xnas/{}/news'.format(current_ticker)
					print('scraping......' + url)
					yield scrapy.Request(url, self.parse)
				except:
					pass
				# print('Sleeping for 10 seconds...')
				# time.sleep(5)

	def parse(self, response):
		# Log repsonse
		self.logger.info('Got successful response from {}'.format(response.url))

		# Grab article headlines
		for headline in response.xpath('//article'):
			l = ItemLoader(item=morningstarNews(), selector=headline)

			l.add_xpath('headline_str', './a/text()')
			l.add_xpath('url', './/a/@href')
			yield l.load_item()