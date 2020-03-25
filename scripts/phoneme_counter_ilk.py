#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Phoneme Counter - Ilokano
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    print('Enter file name/address: ')
    text_address = input()

    phons_in_text = 0               # stores total phonemes in text
    word_phon_count = dict()        # stores count of words with n phonemes
    words_by_phon_count = dict()    # stores lists of words with n phonemes
    phon_dict = dict()              # stores counts of unique phonemes

    word_list = text2wlist(text_address)    # converts text to list of words

    for word in word_list:
        phon_list = word2phon_ilk(word)    # converts word to list of phonemes

        phons_in_text += len(phon_list)

        if len(phon_list) not in word_phon_count:   # initialize count
            word_phon_count[len(phon_list)] = 1
        else:                                       # add 1 to count
            word_phon_count[len(phon_list)] += 1

        if len(phon_list) not in words_by_phon_count:           # initialize list
            words_by_phon_count[len(phon_list)] = [word]
        elif word not in words_by_phon_count[len(phon_list)]:   # append word to list
            words_by_phon_count[len(phon_list)].append(word)

        for phon in phon_list:
            if phon in phon_dict:
                phon_dict[phon] += 1
            else:
                phon_dict[phon] = 1

    # print('\nTotal phonemes in text: ', phons_in_text)

    phon_dict_sorted = {k: phon_dict[k] for k, v in sorted(phon_dict.items(), key=operator.itemgetter(1), reverse=True)}
    # print('\nPhonemes by frequency: ', phon_dict_sorted)
    print('Phoneme        frequency count')
    for item in phon_dict_sorted.items():
        print(item[0] + ' '*(15 - len(item[0])) + str(item[1]))

    # ---- For printing only in output .txt file: ----
    words_by_phon_count_sorted = {k: words_by_phon_count[k] for k in sorted(words_by_phon_count)}
    print('\nList of words by phoneme count: ')
    for item in words_by_phon_count_sorted.items():
        item[1].sort()
        print(item[0], 'phoneme:' if item[0] == 1 else 'phonemes:', item[1], '\n')

    # ---- For printing only in output .txt file: ----
    word_phon_sorted = {k: word_phon_count[k] for k, v in sorted(word_phon_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nFrequency of phonemes per word: ')
    for item in word_phon_sorted.items():
        print(item[1], 'word has' if item[1] == 1 else 'words have', item[0], 'phoneme.' if item[0] == 1 else 'phonemes.')
