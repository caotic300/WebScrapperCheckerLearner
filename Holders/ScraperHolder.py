from Scrappers.Scraper import Scraper

class ScraperHolder():
  def __init__(self):
    self.scrappers = {}

  def add(self, scrapper):
    self.scrappers[scrapper.source] = scrapper

  def remove(self, scrapper_source):
    self.scrappers.pop(scrapper_source)