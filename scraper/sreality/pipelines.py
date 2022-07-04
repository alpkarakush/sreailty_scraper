# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import logging
import os


logger = logging.getLogger('SReality Pipeline')

class SRealityPipeline(object):
    def open_spider(self, spider):
        hostname = os.environ['DB_HOST']
        username = os.environ['DB_USERNAME']
        password = os.environ['DB_PASSWORD']
        database = os.environ['DB_NAME']
        self.connection = psycopg2.connect(host=hostname, 
                                           user=username, 
                                           password=password, 
                                           dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("insert into flats(title,url,img) values(%s,%s,%s)",(item['title'],item['url'],item['img']))
            logger.info(f"Inserting an item into db title:{item['title']} url:{item['url']}")
        except Exception as ex:
            logger.warn(f"Pipeline Error : {str(ex)} --- {str(item)}")
        finally:
            self.connection.commit()
        return item