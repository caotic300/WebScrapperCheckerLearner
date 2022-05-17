from Builders.ScraperBuilder import ScraperBuilder

class DataExtractor():
  """A class that extracts the raw data from a website
  :param scrapper_builder: The scrapper builder holding all the scrappers
  :type ScrapperBuilder"""
  def __init__(self, scrapper_builder):
    self.scrapper_builder = scrapper_builder
    self.data = {}

  def extractData(self):
    """Extracts the raw data"""
    #iterate for all the url scrappers in a source scrapper
    for scrapper_name, scrappers in self.scrapper_builder.scrappers.items():
      data_holder = []
      #print(scrapper_name)
      # initialise selectors for every scrapper in scrappers
      for scrapper in scrappers:

        scrapper.initialiseSelectors()
        scrapper.find_allSelectorsData()
        data = scrapper.alldata
        data_holder.append(data)

      self.data[scrapper_name] = data_holder