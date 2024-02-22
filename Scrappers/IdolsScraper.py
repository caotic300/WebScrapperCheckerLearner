from Scrappers.Scraper import Scraper
from Scrappers.Scraper import Scraper
from Selectors.Selector import Selector
from Selectors.ASelector import ASelector
from Selectors.BSelector import BSelector
from Selectors.BodySelector import BodySelector
from Selectors.DivSelector import DivSelector
from Selectors.H1Selector import H1Selector
from Selectors.H2Selector import H2Selector
from Selectors.H3Selector import H3Selector
from Selectors.H4Selector import H4Selector
from Selectors.H5Selector import H5Selector
from Selectors.H6Selector import H6Selector
from Selectors.HeadSelector import HeadSelector
from Selectors.LiSelector import LiSelector
from Selectors.LinkSelector import LinkSelector
from Selectors.MainSelector import MainSelector
from Selectors.MetaSelector import MetaSelector
from Selectors.NavSelector import NavSelector
from Selectors.PSelector import PSelector
from Selectors.ScriptSelector import ScriptSelector
from Selectors.SectionSelector import SectionSelector
from Selectors.SpanSelector import SpanSelector
from Selectors.TableSelector import TableSelector
from Selectors.TdSelector import TdSelector
from Selectors.ThSelector import ThSelector
from Selectors.TitleSelector import TitleSelector
from Selectors.TrSelector import TrSelector
from Selectors.UlSelector import UlSelector

class IdolsScraper(Scraper):

    def __init__(self, website, parserType="html.parser"):
        super().__init__(website, parserType)


    def initialiseSelectors(self):
        for tag in self.uniquetags:
            if tag in self.selectorOptions:
                if tag == 'ul':
                    self.selectors.append(UlSelector(self.parsedData))
                elif tag == 'li':
                    self.selectors.append(LiSelector(self.parsedData))
                elif tag == 'table':
                    self.selectors.append(TableSelector(self.parsedData))
                elif tag == 'nav':
                    self.selectors.append(NavSelector(self.parsedData))
                elif tag == 'head':
                    self.selectors.append(HeadSelector(self.parsedData))
                elif tag == 'main':
                    self.selectors.append(MainSelector(self.parsedData))
                elif tag == 'p':
                    self.selectors.append(PSelector(self.parsedData))
                elif tag == 'body':
                    self.selectors.append(BodySelector(self.parsedData))
                elif tag == 'div':
                    self.selectors.append(DivSelector(self.parsedData))
                elif tag == 'link':
                    self.selectors.append(LinkSelector(self.parsedData))
                elif tag == 'a':
                    self.selectors.append(ASelector(self.parsedData))
                elif tag == 'b':
                    self.selectors.append(BSelector(self.parsedData))
                elif tag == 'span':
                    self.selectors.append(SpanSelector(self.parsedData))
                elif tag == 'section':
                    self.selectors.append(SectionSelector(self.parsedData))
                elif tag == 'h1':
                    self.selectors.append(H1Selector(self.parsedData))
                elif tag == 'h2':
                    self.selectors.append(H2Selector(self.parsedData))
                elif tag == 'h3':
                    self.selectors.append(H3Selector(self.parsedData))
                elif tag == 'h4':
                    self.selectors.append(H4Selector(self.parsedData))
                elif tag == 'h5':
                    self.selectors.append(H5Selector(self.parsedData))
                elif tag == 'h6':
                    self.selectors.append(H6Selector(self.parsedData))
                #elif tag == 'script':
                    #self.selectors.append(ScriptSelector(self.parsedData))
                #elif tag == 'meta':
                    #self.selectors.append(MetaSelector(self.parsedData))
                elif tag == 'th':
                    self.selectors.append(ThSelector(self.parsedData))
                elif tag == 'tr':
                    self.selectors.append(TrSelector(self.parsedData))
                elif tag == 'td':
                    self.selectors.append(TdSelector(self.parsedData))
                elif tag == 'title':
                    self.selectors.append(TitleSelector(self.parsedData))
                elif tag == 'a':
                    self.selectors.append(ASelector(self.parsedData))
