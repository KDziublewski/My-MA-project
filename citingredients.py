# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CitingredientsSpider(CrawlSpider):
    name = 'citingredients'

    start_urls = ["https://www.chef-in-training.com/"]

    allowed_domains=['chef-in-training.com']

    rules = [

        Rule(

            LinkExtractor(

                allow='chef-in-training.com/*/',

                restrict_css='.more'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.page-number.page-numbers',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.ERSName::text').extract()

            ingredients = response.css('.ingredient::text').extract()

            instructions = response.css('.instruction::text').extract()

            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
