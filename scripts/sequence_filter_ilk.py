#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Sequence Filter - English
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    print('Enter file name/address: ')
    text_address = input()

    word_list = list(set(text2wlist(text_address)))
    # phon_lookup = phon_lookup_eng('cmudict_SPHINX_40.txt')
    # word_phon_dict = {word:word2phon_eng(word,phon_lookup) for word in word_list}

    print('Enter sequence to find: ')
    sequence = input()
    filtered_words = [word for word in word_list if sequence in word]

    print('Enter number of syllables (leave blank for any length): ')
    num_sylls = input()
    if num_sylls is not '':
        num_sylls = int(num_sylls)
        # vowel_list = ['aa', 'ae', 'ah', 'ao', 'aw', 'ay', 'eh', 'er', 'ey', 'ih', 'iy', 'ow', 'oy', 'uh', 'uw']
        # word_syll_count = {word:sum([word_phon_dict[word].count(vowel) for vowel in vowel_list]) for word in filtered_words}
        word_syll_count = {word:len(word2phon_ilk(word)) for word in filtered_words}
        filtered_words = [word for word in filtered_words if word_syll_count[word] == num_sylls]

    print('Enter position of sequence in word (leave blank for any position): ')
    print('1 - start of word')
    print('2 - middle of word')
    print('3 - end of word')
    word_pos = input()
    if word_pos is not '':
        word_pos = int(word_pos)
        seq_len = len(sequence)
        if word_pos == 1:
            filtered_words = [word for word in filtered_words if word[0:seq_len] == sequence]
        elif word_pos == 3:
            filtered_words = [word for word in filtered_words if word[-seq_len:] == sequence]
        else:
            filtered_words = [word for word in filtered_words if (word[0:seq_len] != sequence and word[-seq_len:] != sequence)]

    # print(filtered_words)
    complete_word_list = text2wlist(text_address)
    filtered_word_freq = dict()
    for word in filtered_words:
        filtered_word_freq[word] = complete_word_list.count(word)

    word_freq_sorted = {k: filtered_word_freq[k] for k, v in sorted(filtered_word_freq.items(), key=operator.itemgetter(1), reverse=True)}
    print('Word                frequency')
    for item in word_freq_sorted.items():
        print(item[0] + ' '*(20 - len(item[0])) + str(item[1]))
