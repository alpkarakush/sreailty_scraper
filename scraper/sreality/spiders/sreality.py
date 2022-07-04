import scrapy
import logging
from scrapy.utils.log import configure_logging 

logger = logging.getLogger('SReality Logger')

class SRealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = [
        'https://www.sreality.cz/hledani/prodej/byty?_escaped_fragment_=',
    ]
    
    def __init__(self, *args, **kwargs):
        configure_logging(install_root_handler=False)
        logging.basicConfig(
            filename='log.txt',
            format='%(levelname)s: %(message)s',
            level=logging.INFO
        )
        self.page = 1
        super().__init__(*args, **kwargs)

    def parse(self, response):
        flat_cnt = 0
        
        for flat in response.css('div.property'):
            yield {
                'title': flat.css('span.name::text').get(),
                'url': flat.xpath('.//a/@href').extract_first(),
                'img': flat.xpath('.//img/@src').extract_first()
            }
            flat_cnt += 1
            
            logger.info(f'Flat title:{flat.css("span.name::text").get()} url:{response.css("div.property")[0].xpath(".//a/@href").extract_first()} img:{response.css("div.property")[0].xpath(".//img/@src").extract_first()}')
        
        self.page += 1

        # next_page = response.css('a.paging-next')[0].xpath('@href').get()
        if flat_cnt <= 200:
            yield response.follow('https://www.sreality.cz/hledani/prodej/byty?_escaped_fragment_=&strana={self.page}', self.parse)