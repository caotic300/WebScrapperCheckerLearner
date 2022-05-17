
class URLHolder():
  """A class that holds the different urls for every source"""
  def __init__(self):
    self.urls = {}


  def add(self, url):
    """Adds the url to the urls after checking if the url is in the dictionary"""
    urls = []
    #if url name is in urls names dictionary
    if url.name in self.urls.keys():
      #append the new url to the urls array
      self.urls[url.name].append(url)
    else:
      urls.append(url)
      self.urls[url.name] = urls

  def remove(self, url):
    if url.name in self.urls.keys():
      self.urls[url.name].remove(url.url)
    else:
      self.urls[url.name].remove(url)