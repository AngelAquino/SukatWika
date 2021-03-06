
#!/usr/bin/python3
'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Phoneme Filter - Ilokano
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    print('Enter file name/address: ')
    text_address = input()

    word_list = list(set(text2wlist(text_address)))
    word_phon_dict = {word:word2phon_ilk(word) for word in word_list}

    print('Enter phoneme to find: ')
    selected_phon = input()
    filtered_words = [word for word in word_list if selected_phon in word_phon_dict[word]]

    print('Enter number of syllables (leave blank for any length): ')
    num_sylls = input()
    if num_sylls is not '':
        num_sylls = int(num_sylls)
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'ay', 'aw', 'ey', 'iw', 'oy', 'ow', 'uy']
        word_syll_count = {word:sum([word_phon_dict[word].count(vowel) for vowel in vowel_list]) for word in filtered_words}
        filtered_words = [word for word in filtered_words if word_syll_count[word] == num_sylls]

    print('Enter position of phoneme in word (leave blank for any position): ')
    print('1 - start of word')
    print('2 - middle of word')
    print('3 - end of word')
    word_pos = input()
    if word_pos is not '':
        word_pos = int(word_pos)
        if word_pos == 1:
            filtered_words = [word for word in filtered_words if word_phon_dict[word][0] == selected_phon]
        elif word_pos == 3:
            filtered_words = [word for word in filtered_words if word_phon_dict[word][-1] == selected_phon]
        else:
            filtered_words = [word for word in filtered_words if (word_phon_dict[word][0] != selected_phon and word_phon_dict[word][-1] != selected_phon)]

    # print(filtered_words)
    complete_word_list = text2wlist(text_address)
    filtered_word_freq = dict()
    for word in filtered_words:
        filtered_word_freq[word] = complete_word_list.count(word)

    word_freq_sorted = {k: filtered_word_freq[k] for k, v in sorted(filtered_word_freq.items(), key=operator.itemgetter(1), reverse=True)}
    print('Word                frequency')
    for item in word_freq_sorted.items():
        print(item[0] + ' '*(20 - len(item[0])) + str(item[1]))
