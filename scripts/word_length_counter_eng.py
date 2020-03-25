#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Syllable Counter - English
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    print('Enter file name/address: ')
    text_address = input()

    phon_lookup_address = 'cmudict_SPHINX_40.txt'
    phon_lookup = phon_lookup_eng(phon_lookup_address)

    vowel_list = ['aa', 'ae', 'ah', 'ao', 'aw', 'ay', 'eh', 'er', 'ey', 'ih', 'iy', 'ow', 'oy', 'uh', 'uw']

    sylls_in_text = 0               # stores total syllables in text
    word_syll_count = dict()        # stores count of words with n syllables
    words_by_syll_count = dict()    # stores lists of words with n syllables

    word_list = text2wlist(text_address)    # converts text to list of words

    for word in word_list:
        phon_list = word2phon_eng(word, phon_lookup)     # converts word to list of phonemes


        if len(phon_list) > 0:
            word_vowels = [phon for phon in phon_list if phon in vowel_list]    # lists vowels in word
            # number of syllables = number of vowel phones

            sylls_in_text += len(word_vowels)

            if len(word_vowels) not in word_syll_count:   # initialize count
                word_syll_count[len(word_vowels)] = 1
            else:                                       # add 1 to count
                word_syll_count[len(word_vowels)] += 1

            # if len(word_vowels) not in words_by_syll_count:           # initialize list
            #     words_by_syll_count[len(word_vowels)] = [word]
            # elif word not in words_by_syll_count[len(word_vowels)]:   # append word to list
            #     words_by_syll_count[len(word_vowels)].append(word)

            if len(word_vowels) not in words_by_syll_count:                 # initialize dict
                words_by_syll_count[len(word_vowels)] = {word:1}
            elif word not in words_by_syll_count[len(word_vowels)].keys():  # add word to dict
                words_by_syll_count[len(word_vowels)][word] = 1
            elif word in words_by_syll_count[len(word_vowels)].keys():      # increment word count
                words_by_syll_count[len(word_vowels)][word] += 1

    word_syll_sorted = {k: word_syll_count[k] for k, v in sorted(word_syll_count.items(), key=operator.itemgetter(1), reverse=True)}
    print('\nWord Lengths ')
    for item in word_syll_sorted.items():
        print(item[1], 'word has' if item[1] == 1 else 'words have', item[0], 'syllable.' if item[0] == 1 else 'syllables.')

    # ---- For printing only in output .txt file: ----
    words_by_syll_count_sorted = {k: words_by_syll_count[k] for k in sorted(words_by_syll_count)}
    print('\nList of unique words by syllable count: ')
    for item in words_by_syll_count_sorted.items():
        word_count_sorted = {k: item[1][k] for k in sorted(item[1])}
        print(item[0], 'syllable:' if item[0] == 1 else 'syllables:')
        for i in word_count_sorted.items():
            print(i[0], ':', i[1])
        print('')

    # ---- For printing only in output .txt file: ----
    print('\nTotal syllables in text: ', sylls_in_text)
