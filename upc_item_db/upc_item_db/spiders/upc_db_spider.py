import scrapy
from scrapy import Selector
import time

class LocationsSpider(scrapy.Spider):
    name = "upc_db"

    def start_requests(self):
        # urls = [
        #     'https://www.upcitemdb.com/upc/00888462323772',
        #     'https://www.upcitemdb.com/upc/893265001437'
        #             ]

# THIS IS NEXT THING TO FIX --> fix 429 request : https://github.com/LevPasha/Instagram-API-python/issues/15
# Here: https://stackoverflow.com/questions/43630434/how-to-handle-a-429-too-many-requests-response-in-scrapy/48344232#48344232?newreg=e94604866630416c9147d8cbbbd50b04
# save to file if no pipeline: scrapy crawl upc_db -o real_test_two.jl
# https://docs.google.com/spreadsheets/d/1lLee2QHs4vpcSzL949YFI-Wz3QOhPhFpLffWO8bB3Mg/edit#gid=1357258411

        url_prefix = 'https://www.upcitemdb.com/upc/'
        urls = [
'00017300172714',
'00068981764502',
'00008000945260',
'00052196265312',
'00890551904173'

                                        ]

        for url in urls:
            final_url = url_prefix + url
            # time.sleep(5)
            yield scrapy.Request(url=final_url, callback=self.parse)

        # urls = [
        #
        # ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

    # just ignore all dictionary keys
    def parse(self, response):
        # time.sleep(5)
        divs = response.xpath('//div')
        ols = divs.xpath('//ol')
        upc = response.url.split("/")[-1]
        # related_products = []
        # # https://github.com/scrapy/scrapy/issues/2206
        # for li in response.xpath('//ol/li'):
        #         related_products += Selector(text=li.extract()).xpath('//li/text()').extract()

        #https://www.simplified.guide/scrapy/scrape-table
        table = response.xpath('//*[@class="detail-list"]')
        rows = table.xpath('//tr')
        possible_href = table.xpath('.//a')

        final_yield = {}

        try:
                # !!!!!!!!!!!!!!!!!!!!!!!!!!
                # IF IT DOESN"T HAVE THE 'col-md-6' part....it will fuck up
                # !!!!!!!!!!!!!!!!!!!!!!!!!!
            final_yield['similar_404_upc'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "r", " " ))]//a/text()').getall()
            # final_yield['similar_404_desc'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "r", " " ))]//p/text()').getall()
            final_yield['similar_404_desc'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-6", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "r", " " ))]//p/text()').getall()

            # WE ARE LOSING SOME RELATED PRODUCTS....this is just 
            # word = 'has following Product Name'

            # for y in final_yield['similar_404_desc']:  
            #     print(y)
            #     final_yield['similar_404_desc_clean']= list(filter(lambda x: word not in x, y))


        except IndexError:
        #     # final_yield['upc'] = None
            None

        #upc
        try:
            final_yield['upc'] = upc
        except IndexError:
            # final_yield['upc'] = None
            None

        #product_name
        try:
            final_yield['product_name'] = response.css('title::text').get(),
        except IndexError:
            None

        # all_products
        # try:
        #     final_yield['all_products'] = related_products
        # except IndexError:
        #     # final_yield['upc'] = None
        #     None

        #url
        try:
            final_yield['url'] = response.url
        except IndexError:
            # final_yield['upc'] = None
            None

        # upc-a
        # try:
        #     final_yield[rows[0].xpath('td//text()')[0].extract()] = rows[0].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['one'] = None
        #     None
        #     # print('tble row one empty')

        # EAN-13
        # try:
        #     final_yield[rows[1].xpath('td//text()')[0].extract()] = rows[1].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['two'] = None
        #     None

        # Country of Registration:
        # try:
        #     final_yield[rows[2].xpath('td//text()')[0].extract()] = rows[2].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['three'] = None
        #     None

        # Brand_normal:
        # try:
        #     final_yield[rows[3].xpath('td//text()')[0].extract()] = rows[3].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['four'] = None
        #     None

        # Brand wit Href
        # try:
        #     final_yield['brand_w_href'] = possible_href.css('::text').extract()
        # except IndexError:
        #     # final_yield['five'] = None
        #     None

        # :
        # try:
        #     final_yield[rows[4].xpath('td//text()')[0].extract()] = rows[4].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['six'] = None
        #     None

        # :
        # try:
        #     final_yield[rows[5].xpath('td//text()')[0].extract()] = rows[5].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['seven'] = None
        #     None
        
        # #:
        # try:
        #     final_yield[rows[6].xpath('td//text()')[0].extract()] = rows[6].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['eight'] = None
        #     None
        
        # #:
        # try:
        #     final_yield[rows[7].xpath('td//text()')[0].extract()] = rows[7].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['nine'] = None
        #     None
        
        # #:
        # try:
        #     final_yield[rows[8].xpath('td//text()')[0].extract()] = rows[8].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['ten'] = None
        #     None
        
        # #:
        # try:
        #     final_yield[rows[9].xpath('td//text()')[0].extract()] = rows[9].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['eleven'] = None
        #     None
        
        # #:
        # try:
        #     final_yield[rows[10].xpath('td//text()')[0].extract()] = rows[10].xpath('td//text()')[1].extract()
        # except IndexError:
        #     # final_yield['twelve'] = None
        #     None



        final_yield
        yield final_yield


        # yield {
        #         'upc': upc
        #         # 'title': response.css('title::text').get(),
        #         # rows[0].xpath('td//text()')[0].extract(): rows[0].xpath('td//text()')[1].extract(),   #UPC-A:
        #         # rows[1].xpath('td//text()')[0].extract(): rows[1].xpath('td//text()')[1].extract(),   #EAN-13
        #         # rows[2].xpath('td//text()')[0].extract(): rows[2].xpath('td//text()')[1].extract(),   #Country of Registration:
        #         # 'brand_w_href': possible_href.css('::text').extract(),      #Brand wit Href
        #         # rows[3].xpath('td//text()')[0].extract(): rows[3].xpath('td//text()')[1].extract(), #Brand_normal
        #         # rows[5].xpath('td//text()')[0].extract(): rows[4].xpath('td//text()')[1].extract(),
        #         # rows[5].xpath('td//text()')[0].extract(): rows[5].xpath('td//text()')[1].extract(),
        #         # rows[6].xpath('td//text()')[0].extract(): rows[6].xpath('td//text()')[1].extract()
        #         # rows[7].xpath('td//text()')[0].extract(): rows[7].xpath('td//text()')[1].extract(),
        #         # rows[8].xpath('td//text()')[0].extract(): rows[8].xpath('td//text()')[1].extract(),
        #         # rows[9].xpath('td//text()')[0].extract(): rows[9].xpath('td//text()')[1].extract(),
        #         # rows[10].xpath('td//text()')[0].extract(): rows[10].xpath('td//text()')[1].extract(),
        #         # rows[11].xpath('td//text()')[0].extract(): rows[11].xpath('td//text()')[1].extract(),
        #         # rows[12].xpath('td//text()')[0].extract(): rows[12].xpath('td//text()')[1].extract(),
        #         # 'all_products': related_products,
        #         # 'url': response.url
        #     }
