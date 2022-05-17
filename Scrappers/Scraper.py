from abc import ABC, abstractmethod, abstractproperty
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Scraper(ABC):
    """An abstract class to be subclasses by any class that scraps a website"""
    def __init__(self, website, parserType="html.parser"):
        #website url to select from
        self.website = website
        #scrapper options that are available to scrap from
        self.selectorOptions = ['ul', 'li', 'table', 'nav', 'head', 'main', 'p', 'body', 'div', 'link', 'a', 'b',
                                'span',
                                'section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'th', 'tr', 'td',
                                'title', 'a', 'link'] #'script', 'meta'

        if parserType is not None:
            #create BeatifulSoup object
            self.parsedData = BeautifulSoup(website.data_content(), parserType)
            #all tags from webpage
            self.tags = [tag.name for tag in self.parsedData.find_all(True)]
            #unique tags that are in the webpage
            self.uniquetags = set(self.tags)
        super().__init__()

    @abstractmethod
    def initialiseSelectors(self):
        """A method that initialise the selectors for the different html tags"""
        pass