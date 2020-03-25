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

    for sen_list in par_list:
        for sen in sen_list:
            wlist = sen.split()

            if len(wlist) not in sen_len_count and len(wlist) != 0: # initialize count
                sen_len_count[len(wlist)] = 1
            else:                               # add 1 to count
                sen_len_count[len(wlist)] += 1

    sen_len_sorted = {k: sen_len_count[k] for k, v in sorted(sen_len_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nFrequency of words per sentence: ')
    for item in sen_len_sorted.items():
        print(item[1], 'sentence has' if item[1] == 1 else 'sentences have', item[0], 'word.' if item[0] == 1 else 'words.')
