from Selectors.Selector import Selector
import IllegalArgumentError

class H3Selector(Selector):
  """A class that selects a <h3> tags from a html page"""
  def __init__(self, parsedData):
    self.name = "h3"
    super().__init__(parsedData)

  def find(self):
    return self.parsedData.find_all(self.name)

  def find_by_class_name(self, class_name):
     return self.parsedData.find_all(self.name, class_name)

  def find_by_id(self, id_name):
    return self.parsedData.find_all(self.name, id_name)

  def find_descendants(self, path_to_descendant_tag):
    if self.name not in path_to_descendant_tag:
      raise IllegalArgumentError("The path string passed as argument does not contain a <h3> tag as a parent")
    else:
      return self.parsedData.select(path_to_descendant_tag)