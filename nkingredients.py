# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NkingredientsSpider(CrawlSpider):
    name = 'nkingredients'
    allowed_domains = ['natashaskitchen.com']
    start_urls = ['https://natashaskitchen.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='natashaskitchen.com/(.+)/',

                restrict_css='.title'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.navright',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.wprm-recipe-name::text').extract()

            ingredients = response.css(".wprm-recipe-ingredient-name::text").extract()

            instructions = response.css(".wprm-recipe-instruction-text::text").extract()

            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
