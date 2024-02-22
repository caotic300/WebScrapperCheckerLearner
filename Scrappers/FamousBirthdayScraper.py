from Scrappers.IdolsScraper import IdolsScraper



class FamousBirthdayScraper(IdolsScraper):
    """A scrapper that scraps FamousBirthday website"""
    def __init__(self, website, parserType="html.parser"):
        super().__init__(website, parserType)
        self.selectors = []
        self.alldata = {}
        self.source = 'FamousBirthday'

    def find_allSelectorsData(self):

        for selector in self.selectors:
            self.alldata[selector.name] = selector.find()

    def addSelector(self, selector):
        self.selectors.append(selector)

    def removeSelector(self, selector):
        self.selectors.remove(selector)