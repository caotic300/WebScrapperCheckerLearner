
class Splitter():
    """A Splitter class that splits text data into sentences
    :arg: original_data: The data to be splitted"""
    def __init__(self, original_data):
        self.original_data = original_data
        #self.sentences_by_tags = {}
        self.splitted_data = {}

    def split(self):
        """Splits the text data into sentences and stores it in a dictionary using the source as key and sentences by tag as values"""
        #print(self.original_data)
        sources = self.original_data.keys()
        # for every scrapper key
        for key in sources:
            # get the values for every scrapper url
            values = self.original_data[key]

            sentences_by_tag = {}

            splitted_dict = {}

            #for every data in every scrapper url
            sentences_by_tag = self._get_sentences_by_tag(values)
            splitted_list = []
            for tag, values in sentences_by_tag.items():
                for value in values:
                    #print(value)

                    splitted_values = list(dict.fromkeys(value.split('\n')))
                    #print(splitted_values[0:4])

                    #breakpoint()
                    splitted_list.append(splitted_values)

                splitted_dict[tag] = splitted_list


            final_list = []

            for tag, values in splitted_dict.items():
                for value in values:
                    # print(value)
                    if not final_list or value not in final_list:
                        final_list.append(value)
                        # print(value)
                # print('final_list', final_list)
                sentences_by_tag[tag] = final_list
            self.splitted_data[key] = sentences_by_tag


    def _get_sentences_by_tag(self, values):
        """Retrieves the unique sentences by tag
        :returns sentences_by_tag:  a dictionary containing the tag as key and array of sentences as value"""
        sentences_by_tag = {}
        for value in values:

            # for every html tag and sentences
            for tag, sentences in value.items():
                # append sentences by tag if dictionary not empty and tag is not a key
                if not sentences_by_tag or tag not in sentences_by_tag.keys():
                    sentences_by_tag[tag] = sentences
                # if tag is a key
                elif tag in sentences_by_tag.keys():
                    # get sentences in that tag
                    sentences_in_tags_dict = sentences_by_tag[tag]
                    # sort the sentences
                    sentences_in_tags_dict.sort()
                    # sort the sentences
                    sentences.sort()
                    # if the sentences are not the same contained in the dict

                    if sentences_in_tags_dict != sentences:
                        # append the values
                        # print('sentence inserted', sentences_in_tags_dict)

                        # print('sentence_to_insert', sentences)
                        sentences_by_tag[tag].extend(sentences)
                        # remove duplicate sentences
                        sentences_by_tag[tag] = list(dict.fromkeys(sentences_by_tag[tag]))
                        # print('unique sentences', tags_by_sentences[tag])
                    # break
            # break

        return sentences_by_tag
