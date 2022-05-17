from Scrappers.CompanyScraper import CompanyScraper

class WikiPediaScraper(CompanyScraper):

    def __init__(self, website, parserType="html.parser"):
        super().__init__(website, parserType)
        self.selectors = []
        self.alldata = {}
        self.source = 'Wikipedia'


    def find_allSelectorsData(self):

        for selector in self.selectors:
            self.alldata[selector.name] = selector.find()

    def addSelector(self, selector):
        self.selectors.append(selector)

    def removeSelector(self, selector):
        self.selectors.remove(selector)
