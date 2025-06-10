import scrapy
from abc import ABC

class BaseNovelSpider(scrapy.Spider, ABC):
    """
    Base class for all novel spiders.
    Provides common functionality and structure for scraping novels.
    """

    name = 'base_novel_spider'
    allowed_domains = []
    start_urls = []

    def parse(self, response):
        """
        Default parse method to be overridden by subclasses.
        """
        self.logger.info(f"Parsing response from {response.url}")
        # Implement parsing logic here
        pass

    def handle_error(self, failure):
        """
        Handle errors during requests.
        """
        self.logger.error(f"Request failed: {failure}")
