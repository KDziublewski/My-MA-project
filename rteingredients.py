# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RteingredientsSpider(CrawlSpider):
    name = 'rteingredients'
    allowed_domains = ['recipetineats.com']
    start_urls = ['https://www.recipetineats.com/blog/']

    rules = [

        Rule(

            LinkExtractor(

                allow='recipetineats.com/*/',

                restrict_css='.more-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.pagination-next',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.wprm-recipe-name.wprm-block-text-bold::text').extract()

            ingredients = response.css('.wprm-recipe-ingredient-name::text').extract()

            instructions = response.css('.wprm-recipe-instruction-text').extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
