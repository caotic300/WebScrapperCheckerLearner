from Holders.URLHolder import URLHolder
from Website import Website

class WebsiteBuilder():
  def __init__(self, url_holder):
    self.url_holder =  url_holder
    self.websites = {}

  def create_websites(self):

    for url_name, urls in self.url_holder.urls.items():
      websites = []
      for url in urls:
        website = Website(url.url)
        websites.append(website)
      self.websites[url_name] = websites