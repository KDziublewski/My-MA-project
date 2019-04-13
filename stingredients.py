# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class StingredientsSpider(CrawlSpider):
    name = 'stingredients'

    start_urls = ["https://www.skinnytaste.com/"]

    allowed_domains=['skinnytaste.com']

    rules = [

        Rule(

            LinkExtractor(

                allow='skinnytaste.com/*/',

                restrict_css='.more-link'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.next.page-numbers',))
        	]
    def parse_product(self, response):

            recipe_name = response.xpath('//h1').xpath('text()').extract()

            ingredients = response.css('.ingredient').extract()

            instructions = response.css('.instructions').xpath('ol').xpath('li').extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
