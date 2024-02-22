from Builders.WebsiteBuilder import WebsiteBuilder
from Scrappers.YahooScraper import YahooScraper
from Scrappers.MorningstarScraper import MorningstarScraper
from Scrappers.WikiPediaScraper import WikiPediaScraper
from Scrappers.BloombergScraper import BloombergScraper
from Scrappers.FamousBirthdayScraper import FamousBirthdayScraper
from Scrappers.Scraper import Scraper

class ScraperBuilder():
    def __init__(self, website_builder):
        self.website_builder = website_builder
        self.scrappers = {}

    def create_scrappers(self):

        for website_name, websites in self.website_builder.websites.items():
            scrappers = []
            for website in websites:
                scrapper = self._createScrapper(website_name, website)
                scrappers.append(scrapper)
            self.scrappers[website_name] = scrappers

    def _createScrapper(self, scrapper_type, website):
        #scrapper: Scrapper
        if scrapper_type == 'Morningstar':
            return MorningstarScraper(website)
        elif scrapper_type == 'Yahoo':
            return YahooScraper(website)
        elif scrapper_type == 'Wikipedia':
            return WikiPediaScraper(website)
        elif scrapper_type == 'Bloomberg':
            return BloombergScraper(website)
        elif scrapper_type == 'FamousBirthday':
            return FamousBirthdayScraper(website)
