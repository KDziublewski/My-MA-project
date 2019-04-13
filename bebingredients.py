# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BebingredientsSpider(CrawlSpider):
    name = 'bebingredients'
    allowed_domains = ['browneyedbaker.com']
    start_urls = ['https://www.browneyedbaker.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='browneyedbaker.com/*',

                restrict_css='.more-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.next.page-numbers',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.post-title::text').extract()

            ingredients = response.css(".wprm-recipe-ingredient-name").extract()
            instructions = response.css(".wprm-recipe-instruction-text").extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
