from Selectors.Selector import Selector
import IllegalArgumentError
from Selectors.Selector import Selector

class PSelector(Selector):
  """A class that selects  <p> tags from a html page"""
  def __init__(self, parsedData):
    self.name = "p"
    super().__init__(parsedData)

  def find(self):
    return self.parsedData.find_all(self.name)

  def find_by_class_name(self, class_name):
     return self.parsedData.find_all(self.name, class_name)

  def find_by_id(self, id_name):
    return self.parsedData.find_all(self.name, id_name)

  def find_descendants(self, path_to_descendant_tag):
    if self.name not in path_to_descendant_tag:
      raise IllegalArgumentError("The path string passed as argument does not contain a <p> tag as a parent")
    else:
      return self.parsedData.select(path_to_descendant_tag)