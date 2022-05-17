from abc import ABC, abstractmethod, abstractproperty
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Website:
    def __init__(self, url):
        self.url = url
        self.request = requests.get(url)

    def get_request(self):
        return self.request

    def set_request(self, url):
        self.request = requests.get(url)

    def request_encoding_type(self):
        return self.request.encoding

    def data_content(self):
        return self.request.content

    def data_text(self):
        return self.pageData.text


