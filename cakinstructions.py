# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CakinstructionsSpider(CrawlSpider):
    name = 'cakinstructions'
    allowed_domains = ['cookieandkate.com']
    start_urls = ['https://cookieandkate.com/']

    rules = [

        Rule(

            LinkExtractor(

                allow='cookieandkate.com/*',

                restrict_css='.more-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.pagination-next.alignright',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.entry-title::text').extract()

            ingredients = response.css(".tasty-recipe-ingredients").xpath("ul").xpath("li").extract()

            instructions = response.css(".tasty-recipe-instructions").xpath("ol").xpath("li").extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
