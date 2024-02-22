# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Preprocessors.TextRetriever import TextRetriever
from URL import URL
from Holders.URLHolder import URLHolder
from Builders.WebsiteBuilder import WebsiteBuilder
from Builders.ScraperBuilder import ScraperBuilder
from Preprocessors.DataExtractor import DataExtractor
from Preprocessors.Splitter import Splitter
from CSVFormatter import CSVFormatter
from CSVSaver import CSVSaver
import time
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#def get_uniquer_sentences_by_tag(self, values):

def extract_data_for_company(urls, company_name):
    """Create the different classes to extract the information"""
    company_urlHolder = URLHolder()
    for url in urls:
        company_urlHolder.add(url)

    company_website_builder = WebsiteBuilder(company_urlHolder)
    company_website_builder.create_websites()

    company_scrapper_builder = ScraperBuilder(company_website_builder)
    company_scrapper_builder.create_scrappers()

    company_data_extractor = DataExtractor(company_scrapper_builder)
    company_data_extractor.extractData()

    extracted_data = company_data_extractor.data
    company_text_retriever = TextRetriever(extracted_data)

    text_data = company_text_retriever.get_text()

    splitter = Splitter(text_data)
    splitter.split()

    splitted_data = splitter.splitted_data

    csvFormatter = CSVFormatter(splitted_data, company_name)
    formatted_data = csvFormatter.format()
    return formatted_data

def extract_data_for_idol(urls, idol_name):
    """Create the different classes to extract the information"""
    idol_urlHolder = URLHolder()
    for url in urls:
        idol_urlHolder.add(url)

    idol_website_builder = WebsiteBuilder(idol_urlHolder)
    idol_website_builder.create_websites()

    idol_scrapper_builder = ScraperBuilder(idol_website_builder)
    idol_scrapper_builder.create_scrappers()

    idol_data_extractor = DataExtractor(idol_scrapper_builder)
    idol_data_extractor.extractData()

    extracted_data = idol_data_extractor.data
    idol_text_retriever = TextRetriever(extracted_data)

    text_data = idol_text_retriever.get_text()

    splitter = Splitter(text_data)
    splitter.split()

    splitted_data = splitter.splitted_data

    csvFormatter = CSVFormatter(splitted_data, idol_name)
    formatted_data = csvFormatter.format()
    return formatted_data
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    PYTHONPATH = './Users/pedrojose/PycharmProjects/WebScrapperChecker'
    #URLS of websites

    ## The trade desk URLS
    """TTDmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/ttd/quote'
    TTDmorningstarURLNews = 'https://www.morningstar.com/stocks/xnas/ttd/news'
    TTDyahooURLSummary = 'https://finance.yahoo.com/quote/TTD?p=TTD'
    TTDwikipediaURL = 'https://en.wikipedia.org/wiki/The_Trade_Desk'
    TTDBloombergURL = 'https://www.bloomberg.com/quote/TTD:US'"""
    
    FamousBirthdayURL = 'https://www.famousbirthdays.com/people/olivia-rodrigo.html'
    FamousBirthdayURL_two = 'https://www.famousbirthdays.com/people/olivia-rodrigo.html'
    # Creating the urls objets
    #TTD_morningstar_url_quote = URL('Morningstar', TTDmorningstarURLQuote)
    #TTD_morningstar_url_news = URL('Morningstar', TTDmorningstarURLNews)
    #TTD_yahoo_url = URL('Yahoo', TTDyahooURLSummary)
    #TTD_wikipedia_url = URL('Wikipedia', TTDwikipediaURL)
    FamousBirthday_url = URL('FamousBirthday', FamousBirthdayURL)
    #TTD_bloomberg_url = URL('Bloomberg', TTDBloombergURL)
    FamousBirthday_url_rihana = URL('FamousBirthday', FamousBirthdayURL_two)
    #all urls for TTD company
    olivia_rodrigo_urls = [FamousBirthday_url]

    rihana_urls = [FamousBirthday_url_rihana]
    """ttd_urls = [TTD_morningstar_url_quote,
                TTD_morningstar_url_news,
                TTD_yahoo_url,
                TTD_wikipedia_url]#,
                #TTD_bloomberg_url]"""

    #Apple Inc Urls
    """ApplemorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/aapl/quote'
    ApplewikipediaURL = 'https://en.wikipedia.org/wiki/Apple_Inc.'
    AppleyahooURLSummary = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
    AppleyahooURLProfile = 'https://finance.yahoo.com/quote/AAPL/profile?p=AAPL'
    #AppleBloombergURL = 'https://www.bloomberg.com/quote/AAPL:US'

    # Creating the urls objets
    Apple_morningstar_url_quote = URL('Morningstar', ApplemorningstarURLQuote)
    Apple_yahoo_url = URL('Yahoo', AppleyahooURLSummary)
    Apple_yahoo_url_profile = URL('Yahoo', AppleyahooURLProfile)
    Apple_wikipedia_url = URL('Wikipedia', ApplewikipediaURL)
    #Apple_bloomberg_url = URL('Bloomberg', AppleBloombergURL)

    # all urls for Apple company
    apple_urls = [Apple_morningstar_url_quote,
                  Apple_yahoo_url,
                  Apple_yahoo_url_profile,
                  Apple_wikipedia_url]#,
                  #Apple_bloomberg_url]

    #Microsoft Inc Urls
    MicrosoftmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/msft/quote'
    MicrosoftwikipediaURL = 'https://en.wikipedia.org/wiki/Microsoft'
    MicrosoftyahooURLSummary = 'https://finance.yahoo.com/quote/MSFT/?p=MSFT'
    MicrosoftyahooURLProfile = 'https://finance.yahoo.com/quote/MSFT/profile?p=MSFT'
    #MicrosoftBloombergURL = 'https://www.bloomberg.com/quote/MSFT:US'
    # Creating the urls objets
    Microsoft_morningstar_url_quote = URL('Morningstar', MicrosoftmorningstarURLQuote)
    Microsoft_yahoo_url = URL('Yahoo', MicrosoftyahooURLSummary)
    Microsoft_yahoo_url_profile = URL('Yahoo', MicrosoftyahooURLProfile)
    Microsoft_wikipedia_url = URL('Wikipedia', MicrosoftwikipediaURL)
    #Microsoft_bloomberg_url = URL('Bloomberg', MicrosoftBloombergURL)

    # all urls for Microsoft company
    microsoft_urls = [Microsoft_morningstar_url_quote,
                      Microsoft_yahoo_url,
                      Microsoft_yahoo_url_profile,
                      Microsoft_wikipedia_url]#,
                      #Microsoft_bloomberg_url]

    #Amazon Inc Urls
    AmazonmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/amzn/quote'
    AmazonyahooURLSummary = 'https://finance.yahoo.com/quote/AMZN/'
    AmazonyahooURLProfile = 'https://finance.yahoo.com/quote/AMZN/profile?p=AMZN'
    AmazonwikipediaURL = 'https://en.wikipedia.org/wiki/Amazon_(company)'
    #AmazonBloombergURL = 'https://www.bloomberg.com/quote/AMZN:US'

    # Creating the urls objets
    Amazon_morningstar_url_quote = URL('Morningstar', AmazonmorningstarURLQuote)
    Amazon_yahoo_url = URL('Yahoo', AmazonyahooURLSummary)
    Amazon_yahoo_url_profile = URL('Yahoo', AmazonyahooURLProfile)
    Amazon_wikipedia_url = URL('Wikipedia', AmazonwikipediaURL)
    #Amazon_bloomberg_url = URL('Bloomberg', AmazonBloombergURL)

    # all urls for Amazon company
    amazon_urls = [Amazon_morningstar_url_quote,
                   Amazon_yahoo_url,
                   Amazon_yahoo_url_profile,
                   Amazon_wikipedia_url]#,
                   #Amazon_bloomberg_url]
    #Google
    GooglemorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/amzn/quote'
    GoogleyahooURLSummary = 'https://finance.yahoo.com/quote/GOOG?p=GOOG'
    GoogleyahooURLProfile = 'https://finance.yahoo.com/quote/AMZN/profile?p=AMZN'
    GooglewikipediaURL = 'https://en.wikipedia.org/wiki/Google'
    #GoogleBloombergURL = 'https://www.bloomberg.com/quote/GOOG:US'

    # Creating the urls objets
    Google_morningstar_url_quote = URL('Morningstar', GooglemorningstarURLQuote)
    Google_yahoo_url = URL('Yahoo', GoogleyahooURLSummary)
    Google_yahoo_url_profile = URL('Yahoo', GoogleyahooURLProfile)
    Google_wikipedia_url = URL('Wikipedia', GooglewikipediaURL)
    #Google_bloomberg_url = URL('Bloomberg', GoogleBloombergURL)

    # all urls for Google company
    google_urls = [Google_morningstar_url_quote,
                   Google_yahoo_url,
                   Google_yahoo_url_profile,
                   Google_wikipedia_url]#,
                   #Google_bloomberg_url]
    #Pinterest
    PinterestmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnys/pins/quote'
    PinterestyahooURLSummary = 'https://finance.yahoo.com/quote/PINS/'
    PinterestyahooURLProfile = 'https://finance.yahoo.com/quote/PINS/profile?p=PINS'
    PinterestwikipediaURL = 'https://en.wikipedia.org/wiki/Pinterest'
    #PinterestBloombergURL = 'https://www.bloomberg.com/quote/PINS:US'

    # Creating the urls objets
    Pinterest_morningstar_url_quote = URL('Morningstar', PinterestmorningstarURLQuote)
    Pinterest_yahoo_url = URL('Yahoo', PinterestyahooURLSummary)
    Pinterest_yahoo_url_profile = URL('Yahoo', PinterestyahooURLProfile)
    Pinterest_wikipedia_url = URL('Wikipedia', PinterestwikipediaURL)
    #Pinterest_bloomberg_url = URL('Bloomberg', PinterestBloombergURL)

    # all urls for Pinterest company
    pinterest_urls = [Pinterest_morningstar_url_quote,
                      Pinterest_yahoo_url,
                      Pinterest_yahoo_url_profile,
                      Pinterest_wikipedia_url]#,
                      #Pinterest_bloomberg_url]

    # Atlassian
    AtlassianmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnys/team/quote'
    AtlassianyahooURLSummary = 'https://finance.yahoo.com/quote/TEAM?p=TEAM'
    AtlassianyahooURLProfile = 'https://finance.yahoo.com/quote/TEAM/profile?p=TEAM'
    AtlassianwikipediaURL = 'https://en.wikipedia.org/wiki/Atlassian'
    #AtlassianBloombergURL = 'https://www.bloomberg.com/quote/TEAM:US'

    # Creating the urls objets
    Atlassian_morningstar_url_quote = URL('Morningstar', AtlassianmorningstarURLQuote)
    Atlassian_yahoo_url = URL('Yahoo', AtlassianyahooURLSummary)
    Atlassian_yahoo_url_profile = URL('Yahoo', AtlassianyahooURLProfile)
    Atlassian_wikipedia_url = URL('Wikipedia', AtlassianwikipediaURL)
    #Atlassian_bloomberg_url = URL('Bloomberg', AtlassianBloombergURL)

    # all urls for Atlassian company
    atlassian_urls = [Atlassian_morningstar_url_quote,
                      Atlassian_yahoo_url,
                      Atlassian_yahoo_url_profile,
                      Atlassian_wikipedia_url]#,
                      #Atlassian_bloomberg_url]

    #Netflix
    NetflixmorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/nflx/quote'
    NetflixyahooURLSummary = 'https://finance.yahoo.com/quote/NFLX?p=NFLX'
    NetflixyahooURLProfile = 'https://finance.yahoo.com/quote/NFLX/profile?p=NFLX'
    NetflixwikipediaURL = 'https://en.wikipedia.org/wiki/Netflix'
    #NetflixBloombergURL = 'https://www.bloomberg.com/quote/NFLX:US'

    # Creating the urls objets
    Netflix_morningstar_url_quote = URL('Morningstar', NetflixmorningstarURLQuote)
    Netflix_yahoo_url = URL('Yahoo', NetflixyahooURLSummary)
    Netflix_yahoo_url_profile = URL('Yahoo', NetflixyahooURLProfile)
    Netflix_wikipedia_url = URL('Wikipedia', NetflixwikipediaURL)
    #Netflix_bloomberg_url = URL('Bloomberg', NetflixBloombergURL)

    # all urls for Netflix company
    netflix_urls = [Netflix_morningstar_url_quote,
                    Netflix_yahoo_url,
                    Netflix_yahoo_url_profile,
                    Netflix_wikipedia_url]#,
                    #Netflix_bloomberg_url]

    # NVIDIA
    NvidiamorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/nvda/quote'
    NvidiayahooURLSummary = 'https://finance.yahoo.com/quote/NVDA?p=NVDA'
    NvidiayahooURLProfile = 'https://finance.yahoo.com/quote/NVDA/profile?p=NVDA'
    NvidiawikipediaURL = 'https://en.wikipedia.org/wiki/Nvidia'
    #NvidiaBloombergURL = 'https://www.bloomberg.com/quote/NVDA:US'

    # Creating the urls objets
    Nvidia_morningstar_url_quote = URL('Morningstar', NvidiamorningstarURLQuote)
    Nvidia_yahoo_url = URL('Yahoo', NvidiayahooURLSummary)
    Nvidia_yahoo_url_profile = URL('Yahoo', NvidiayahooURLProfile)
    Nvidia_wikipedia_url = URL('Wikipedia', NvidiawikipediaURL)
    #Nvidia_bloomberg_url = URL('Bloomberg', NvidiaBloombergURL)

    # all urls for Nvidia company
    nvidia_urls = [Nvidia_morningstar_url_quote,
                   Nvidia_yahoo_url,
                   Nvidia_yahoo_url_profile,
                   Nvidia_wikipedia_url]#,
                   #Nvidia_bloomberg_url]

    # Adobe
    AdobemorningstarURLQuote = 'https://www.morningstar.com/stocks/xnas/adbe/quote'
    AdobeyahooURLSummary = 'https://finance.yahoo.com/quote/ADBE?p=ADBE'
    AdobeyahooURLProfile = 'https://finance.yahoo.com/quote/ADBE/profile?p=ADBE'
    AdobewikipediaURL = 'https://en.wikipedia.org/wiki/Adobe_Inc.'
    #AdobeBloombergURL = 'https://www.bloomberg.com/quote/ADBE:US'


    # Creating the urls objets
    Adobe_morningstar_url_quote = URL('Morningstar', AdobemorningstarURLQuote)
    Adobe_yahoo_url = URL('Yahoo', AdobeyahooURLSummary)
    Adobe_yahoo_url_profile = URL('Yahoo', AdobeyahooURLProfile)
    Adobe_wikipedia_url = URL('Wikipedia', AdobewikipediaURL)
    #Adobe_bloomberg_url = URL('Bloomberg', AdobeBloombergURL)

    # all urls for Adobe company
    adobe_urls = [Adobe_morningstar_url_quote,
                  Adobe_yahoo_url,
                  Adobe_yahoo_url_profile,
                  Adobe_wikipedia_url]#,
                  #Adobe_bloomberg_url]"""


    # store starting time
    #begin = time.time()
    formatted_data = [extract_data_for_idol(olivia_rodrigo_urls, 'Olivia Rodrigo'), 
                      extract_data_for_idol(rihana_urls, 'Rihana')]
    """formatted_data = [extract_data_for_company(ttd_urls, 'The Trade Desk'),
                      extract_data_for_company(apple_urls, 'Apple Inc'),
                      extract_data_for_company(microsoft_urls, 'Microsoft'),
                      extract_data_for_company(amazon_urls, 'Amazon Inc'),
                      extract_data_for_company(google_urls, 'Google Inc'),
                      extract_data_for_company(pinterest_urls, 'Pinterest Inc'),
                      extract_data_for_company(atlassian_urls, 'Atlassian Inc'),
                      extract_data_for_company(netflix_urls, 'Netflix Inc'),
                      extract_data_for_company(nvidia_urls, 'Nvidia Inc'),
                      extract_data_for_company(adobe_urls, 'Adobe Inc'),
                      ]"""

    final_formatted_data = []
    #print(formatted_data)

    for idol_data in formatted_data:
        for idol_row in idol_data:
            #print(company_data)

            final_formatted_data.append(idol_row)

    #find columns to find
    cols = list(final_formatted_data[0].keys())
    file_name = 'idol_data_updated_t.csv'#'company_data.csv'#
    csvSaver = CSVSaver(final_formatted_data, file_name, cols)
    csvSaver.convert()

   # time.sleep(1)
    # store end time
    #end = time.time()

    # total time taken
    #print(f"Total runtime of the program is {end - begin}")



