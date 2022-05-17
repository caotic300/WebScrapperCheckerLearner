from abc import ABC, abstractmethod, abstractproperty
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Selector(ABC):
    """An Abstract class that describes the behavior of a selector"""

    def __init__(self, parsedData):
        self.parsedData = parsedData
        # self.descendants = parsedData.descendants

    @abstractmethod
    def find(self):
        """Finds all the specific tags specified by the implementing subclass
           Returns:  a list of tags
           """
        pass

    @abstractmethod
    def find_by_class_name(self, class_name):
        """Finds all the tags specified by the implementing subclass containing a class_name
           Returns:  a list of tags containing the same class_name
        """
        pass

    @abstractmethod
    def find_by_id(self, id_name):
        """Finds all the tags specified by the implementing subclass containing an id_name
           Returns:  a list of tags containing the same id_name
        """
        pass

    @abstractmethod
    def find_descendants(self, path_to_descendant_tag):
        """Finds all the tags specified by the implementing subclass containing an id name
           Returns:  a list containing the descendants of a tag
        """
        pass
