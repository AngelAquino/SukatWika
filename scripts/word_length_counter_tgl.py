#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Syllable Counter - Tagalog/Cebuano
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    print('Enter file name/address: ')
    text_address = input()

    sylls_in_text = 0               # stores total syllables in text
    word_syll_count = dict()        # stores count of words with n syllables
    words_by_syll_count = dict()    # stores lists of words with n syllables
    syll_dict = dict()              # stores counts of unique syllables

    word_list = text2wlist(text_address)    # converts text to list of words

    for word in word_list:
        syll_list = word2syll_tgl(word)     # converts word to list of syllables

        sylls_in_text += len(syll_list)

        if len(syll_list) not in word_syll_count:   # initialize count
            word_syll_count[len(syll_list)] = 1
        else:                                       # add 1 to count
            word_syll_count[len(syll_list)] += 1

        if len(syll_list) not in words_by_syll_count:           # initialize list
            words_by_syll_count[len(syll_list)] = [word]
        elif word not in words_by_syll_count[len(syll_list)]:   # append word to list
            words_by_syll_count[len(syll_list)].append(word)

        for syll in syll_list:
            if syll in syll_dict:
                syll_dict[syll] += 1
            else:
                syll_dict[syll] = 1

    word_syll_sorted = {k: word_syll_count[k] for k, v in sorted(word_syll_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nWord Lengths ')
    for item in word_syll_sorted.items():
        print(item[1], 'word has' if item[1] == 1 else 'words have', item[0], 'syllable.' if item[0] == 1 else 'syllables.')

    # ---- For printing only in output .txt file: ----
    words_by_syll_count_sorted = {k: words_by_syll_count[k] for k in sorted(words_by_syll_count)}
    print('\nList of unique words by syllable count: ')
    for item in words_by_syll_count_sorted.items():
        item[1].sort()
        print(item[0], 'syllable:' if item[0] == 1 else 'syllables:', item[1], '\n')

    # ---- For printing only in output .txt file: ----
    print('\nTotal syllables in text: ', sylls_in_text)
