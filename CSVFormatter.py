class CSVFormatter():
    """A class that formats the data into an CSV file"""

    def __init__(self, data, name):
        self.data = data
        self.company_name = name

    def format(self):
        """Formats the data into a dictionary containing columns and rows"""
        sentences_by_tag = []
        csv_sentences_tags_formatted = []
        formatted_dict = {}

        source_tag_sentences_dict = {}

        for source, sentences_in_source in self.data.items():

            # sentences
            # print(sentences_in_source.values())
            # breakpoint()
            for tag, sentences_in_tag in sentences_in_source.items():
                # print(tag, sentences_in_tag)
                # breakpoint()
                # print(tag)
                # break
                #source_tag_sentences_dict[(source, tag)] = sentences_in_tag
            # print(source_tag_sentences_dict)
            # breakpoint()
                if (source, tag) not in formatted_dict:
                    source_tag_sentences_dict[(self.company_name, source, tag)] = sentences_in_tag
                else:
                    source_tag_sentences_dict[(self.company_name, source, tag)].extend(sentences_in_tag)

            # print(source, tag, sentences_in_tag)
            # for sentences in sentences_in_tag:
            #     #print(sentences)
            #     #breakpoint()
            #     if (self.company_name, source, tag) not in formatted_dict:
            #         formatted_dict[(self.company_name, source, tag)] = sentences
            #     else:
            #         formatted_dict[(self.company_name, source, tag)].extend(sentences)
            # print(formatted_dict)
            # breakpoint()
        i = 0
        # for (source, tag) in source_tag_sentences_dict.keys():
        #     # print(sentences_in_tag)
        #     # print(tag)
        #     # breakpoint()
        #     sentences_in_tag = source_tag_sentences_dict[(source, tag)]
        #     for sentences in sentences_in_tag:
        #         print(sentences)
        #         if i > 2:
        #             breakpoint()
                # sentences_by_tag
                #print(sentences)
                #breakpoint()
                #if (source, tag) not in formatted_dict:
                #formatted_dict[(source, tag)] = sentences
                #sentences_by_tag.append(sentences)
                #else:
                #    formatted_dict[(source, tag)].extend(sentences)

                # formatted_dict[(source, tag)] = sentences
            # print(formatted_dict.values())
            # print(formatted_dict.keys())
            # i += 1
            # if i > 2:
            # breakpoint()
            # else:
            #    formatted_dict[(self.company_name, source, tag)].extend(sentences)
            # if (source, tag) not in formatted_dict:
            #     formatted_dict[(self.company_name, source, tag)] = sentences
            # else:
            #     formatted_dict[(self.company_name, source, tag)].extend(sentences)

        sentences_included_by_source = {}
        source_set = set()
        sentences_set_source = set()
        # i = 0
        for cols, rows in source_tag_sentences_dict.items():
            #print(sentences)
            # break
            #print(cols)
            #breakpoint()
            #print(rows)

            #sentences_dict = {}
            #iterate through the sentenses
            for sentences in rows:
                #print(sentences)
                #breakpoint()
                #for sentence in sentences:
                sentences_by_tag.append({'company_name': cols[0], 'source': cols[1], 'tag': cols[2], 'text': sentences})
                #print(sentences_tags)

        for csv_row in sentences_by_tag:
            print(csv_row)
            # csv_sentences_tags_formatted.append(
            #                  {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
            #                   'text': csv_row['text']})
            # print(csv_sentences_tags_formatted)

            for sentence in csv_row['text']:
                csv_sentences_tags_formatted.append(
                    {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
                     'text': sentence})
                #print(csv_sentences_tags_formatted)
                #breakpoint()
        # for (source, tag) in formatted_dict.keys():
        #
        #     # WORKS 1
        #     # if source not in source_set:
        #     #     tag_sentence_set = set()
        #     # else:
        #     sentences = formatted_dict[(source, tag)]
        #     for sentence in sentences:
        #         print(sentence)
        #         # breakpoint()
        #         csv_sentences_tags_formatted.append(
        #             {'company_name': self.company_name, 'source': source, 'tag': tag,
        #              'text': sentence})
                # print(csv_sentences_tags_formatted)
                # sentences_by_tag[]
                # if (tag, sentence) not in tag_sentence_set:
                # print({'company_name': company_name, 'source':source, 'tag': tag,
                #                'text': sentence})
                #   tag_sentence_set.add((tag, sentence))
                # #print(sentence)
                # print({'company_name': company_name, 'source':source, 'tag': tag,
                #                        'text': sentence})
                # #sentences_by_tag.append({'company_name':company_name, 'source':source, 'tag':tag, 'text': sentence})
                # #if source in source_set:
                #    # if sentence not in sentences_set_source:
                # csv_sentences_tags_formatted.append(
                #                     {'company_name': company_name, 'source':source, 'tag': tag,
                #                                    'text': sentence})
                # sentences_set_source.add(sentence)

                # sentences_included_by_source[source] = sentences_set_source
                # else:
            #     csv_sentences_tags_formatted.append(
            #         {'company_name': company_name, 'source': source, 'tag': tag,
            #          'text': sentence})
            #     source_set.add(source)
            #     sentences_set_source.clear()
            # print(csv_sentences_tags_formatted)

        # for csv_row in sentences_by_tag:
        #     # print(csv_row)
        #     # csv_sentences_tags_formatted.append(
        #     #                  {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
        #     #                   'text': csv_row['text']})
        #     # print(csv_sentences_tags_formatted)
        #
        #     for sentence in csv_row['text']:
        #         csv_sentences_tags_formatted.append(
        #             {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
        #              'text': sentence})
        #         print(csv_sentences_tags_formatted)

        #         #breakpoint()
        #         #for sentence in sentences:
        #         #formatted_dict[(self.company_name, source, tag)] = sentences


        # sotre sentences as key using the source, company name and tag

        # tags_by_sentence.extend(sentence)
        # print(tags_by_sentence)
        # breakpoint()
        # print(tags_by_sentence)
        # if i > 5:
        #     breakpoint()
        # i += 1
        # breakpoint()

        # formatted_dict[index] = (self.company_name, source, tag, tags_by_sentence)
        # sentences_tags.append((self.company_name, source, tag, tags_by_sentence))
        # if index > 2:
        #     #print(tags_by_sentence)
        #     print(sentences_tags[0:1])
        #     breakpoint()
        # for sentence in tags_by_sentence:
        #     csv_sentences_tags_formatted.append(
        #         {'company_name': self.company_name, 'source':source, 'tag': tag,
        #             'text': sentence})
        #     print(csv_sentences_tags_formatted)
        #     breakpoint()
        # formatted_dict[(self.company_name, source, tag)] = sentence
        # print('sentences --------', sentencesHolder[1])
        # print('tag --------', tag)
        # print(formatted_dict)

        # get the columns and rows to create the row
        # for cols, rows in formatted_dict.items():
        #     #print(sentences)
        #     # break
        #     #print(cols)
        #     #breakpoint()
        #     #print(rows)
        #
        #     #sentences_dict = {}
        #     #iterate through the sentenses
        #     for sentences in rows:
        #         #print(sentences)
        #
        #         #for sentence in sentences:
        #         sentences_by_tags.append({'company_name': cols[0], 'source': cols[1], 'tag': cols[2], 'text': sentences})
        #         print(sentences_tags)
        # breakpoint()
        # sentences_tags.append(sentences)

        # for csv_row in sentences_by_tag:
        #     print(csv_row)
        #     csv_sentences_tags_formatted.append(
        #                      {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
        #                       'text': csv_row['text']})
        #     print(csv_sentences_tags_formatted)
        #
        #     for sentence in csv_row['text']:
        #         csv_sentences_tags_formatted.append(
        #             {'company_name': csv_row['company_name'], 'source': csv_row['source'], 'tag': csv_row['tag'],
        #              'text': sentence})
        #         print(csv_sentences_tags_formatted)
        #         breakpoint()

        return csv_sentences_tags_formatted  # sentences_tags#
