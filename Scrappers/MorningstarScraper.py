from Scrappers.CompanyScraper import CompanyScraper



class MorningstarScraper(CompanyScraper):
    """A scrapper that scraps Morningstar website"""
    def __init__(self, website, parserType="html.parser"):
        super().__init__(website, parserType)
        self.selectors = []
        self.alldata = {}
        self.source = 'Morningstar'

    def find_allSelectorsData(self):

        for selector in self.selectors:
            self.alldata[selector.name] = selector.find()

    def addSelector(self, selector):
        self.selectors.append(selector)

    def removeSelector(self, selector):
        self.selectors.remove(selector)