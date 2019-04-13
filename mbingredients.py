# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MbingredientsSpider(CrawlSpider):
    name = 'mbingredients'
    allowed_domains = ['minimalistbaker.com']
    start_urls = ['https://minimalistbaker.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='minimalistbaker.com/*',

                restrict_css='.more-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.pagination-next',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.wprm-recipe-name::text').extract()

            ingredients = response.css(".wprm-recipe-ingredient-name::text").extract()

            instructions = response.css(".wprm-recipe-instruction-text::text").extract()

            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
