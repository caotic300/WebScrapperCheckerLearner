
class TextRetriever():
    def __init__(self, data):
        self.data = data
        self.data_kwrds = data.keys()
        self.data_values = data.values()

    def get_text(self):
        scrappers_by_source = self.data

        scrapper_data = {}

        #breakpoint()
        #get all website scrappers and website source

        for key, scrappers in scrappers_by_source.items():
            text_data_by_scrapper = []
            #print(key)
            #print(scrappers)

            #for all scrapper in a website
            for scrapper in scrappers:
                # print(scrapper)
                text_data = {}
                #for the data in each scrapper, having tag and data
                for tag, data in scrapper.items():
                    # print(key, data)
                    # list to store sentences
                    sentences = list()
                    # for all the sentences in the data
                    for sentence in data:
                        # extract the text of all the data, and append it to sentences

                        sentence = sentence.get_text(separator='\n', strip=True)

                        # if 'Ali Mogharabi' in sentence and key == 'Yahoo':
                        #     print(sentence)

                        sentences.append(sentence)
                    # store only the unique sentences only
                    unique_sentences = list(dict.fromkeys(sentences))
                    # if the tag is in the text_data
                    if tag in text_data.keys():
                        #append the new unique sentences
                        text_data[tag].append(unique_sentences)
                    else:
                        #add the new tag and unique sentences
                        text_data[tag] = unique_sentences
                    # append the text data
                    text_data_by_scrapper.append(text_data)

            scrapper_data[key] = text_data_by_scrapper

        #for text in scrapper_data['Morningstar']:
        #print()
        #print()
        #print(scrapper_data['Yahoo'][0:5])
        return scrapper_data