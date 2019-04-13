import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BBSpider(CrawlSpider):

    name = 'BudgetBytesIngredients'

    start_urls = ["https://www.budgetbytes.com/category/recipes/"]

    allowed_domains=["budgetbytes.com"]

    rules = [

        Rule(

            LinkExtractor(

                allow='budgetbytes.com/(.+)/',

                restrict_css='.archive-post'),

            callback='parse_recipe'),

        Rule(

            LinkExtractor(

                allow='/page/\d+',

                restrict_css='.page-numbers',))
        	]
    def parse_recipe(self, response):

            recipe_name = response.css('.title::text').extract()

            ingredients = response.css(".wprm-recipe-ingredient-name::text").extract()

            instructions = response.css(".wprm-recipe-instructions").xpath("li").xpath("div").xpath("text()").extract()
            yield {"Recipe Name":recipe_name,"Ingredients":ingredients,"Instructions":instructions}
