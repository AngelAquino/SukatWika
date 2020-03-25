#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Sentence and Paragraph Counter
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    par_len_count = dict()  # stores count of paragraphs with n sentences
    sen_len_count = dict()  # stores count of sentences with n words

    print('Enter file name/address: ')
    text_address = input()

    par_list = text2pslist(text_address)
    print(par_list)

    for sen_list in par_list:
        if len(sen_list) not in par_len_count:  # initialize count
            par_len_count[len(sen_list)] = 1
        else:                                   # add 1 to count
            par_len_count[len(sen_list)] += 1

        for sen in sen_list:
            wlist = sen.split()

            if len(wlist) not in sen_len_count: # initialize count
                sen_len_count[len(wlist)] = 1
            else:                               # add 1 to count
                sen_len_count[len(wlist)] += 1

    print('\nTotal paragraphs in text: ', len(par_list))

    par_len_sorted = {k: par_len_count[k] for k, v in sorted(par_len_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nFrequency of sentences per paragraph: ')
    for item in par_len_sorted.items():
        print(item[0], 'sentence:' if item[0] == 1 else 'sentences:', item[1], 'paragraph' if item[1] == 1 else 'paragraphs')

    sen_len_sorted = {k: sen_len_count[k] for k, v in sorted(sen_len_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nFrequency of words per sentence: ')
    for item in sen_len_sorted.items():
        print(item[0], 'word:' if item[0] == 1 else 'words:', item[1], 'sentence' if item[1] == 1 else 'sentences')
