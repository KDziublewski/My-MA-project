# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FfmingredientsSpider(CrawlSpider):
    name = 'ffmingredients'
    allowed_domains = ['familyfreshmeals.com']
    start_urls = ['https://www.familyfreshmeals.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='familyfreshmeals.com/*',

                restrict_css='.entry-title-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.pagination-next.alignright',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.ERSName::text').extract()

            ingredients = response.css(".ingredient::text").extract()

            instructions = response.css(".instruction::text").extract()

            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
