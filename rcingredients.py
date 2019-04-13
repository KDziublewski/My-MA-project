import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RcingredientsSpider(CrawlSpider):
    name = 'rcingredients'

    start_urls = ["https://therecipecritic.com/"]

    allowed_domains=[]

    rules = [

        Rule(

            LinkExtractor(

                allow='recipecritic.com/*',

                restrict_css='.entry-title'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.next.page-numbers',))
        	]
    def parse_product(self, response):

            recipe_name = response.css('.entry-title::text').extract()

            ingredients = response.css(".ingredient::text").extract()

            instructions = response.css(".instruction").extract()

            yield {"RecipeName":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
