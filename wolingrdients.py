# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WolingrdientsSpider(CrawlSpider):
    name = 'wolingrdients'
    allowed_domains = ['thewoksoflife.com']
    start_urls = ['https://thewoksoflife.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='thewoksoflife.com/*',

                restrict_css='.entry-title-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.pagination-next',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.ERSName::text').extract()

            ingredients = response.css(".ingredient").extract()

            instructions = response.css(".instruction::text").extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
