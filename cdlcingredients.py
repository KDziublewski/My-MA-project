# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CdlcingredientsSpider(CrawlSpider):
    name = 'cdlcingredients'
    allowed_domains = ['lecremedelacrumb.com']
    start_urls = ['https://www.lecremedelacrumb.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='lecremedelacrumb.com/(.+)/',

                restrict_css='.entry-title.alt-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.next.page-numbers',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.wprm-recipe-name::text').extract()

            ingredients = response.css(".wprm-recipe-ingredient-name::text").extract()

            instructions = response.css(".wprm-recipe-instruction-text").xpath("p").xpath("text()").extract()

            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
