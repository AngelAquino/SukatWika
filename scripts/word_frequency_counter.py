'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Word Frequency Counter
'''

if __name__ == '__main__':
    from parsing_functions import *
    import operator

    word_freq_count = dict()  # stores frequency per word

    print('Enter file name/address: ')
    text_address = input()

    word_list = text2wlist(text_address)
    word_set = list(set(word_list))
    remove_set = list()

    for word in word_set:
        if any(char.isdigit() for char in word) or len(word) <= 1:
            remove_set.append(word)
        else:
            word_freq_count[word] = word_list.count(word)

    for word in remove_set:
        word_set.remove(word)

    print('\nSort alphabetically (default) or by frequency?')
    print('A - alphabetically')
    print('F - by frequency')
    sort_type = input()

    print('\nFrequency of words in text: ')
    if sort_type == 'F':
        word_freq_sorted = {k: word_freq_count[k] for k, v in sorted(word_freq_count.items(), key=operator.itemgetter(1), reverse=True)}
        print('Word                frequency')
        for item in word_freq_sorted.items():
            print(item[0] + ' '*(20 - len(item[0])) + str(item[1]))
    else:
        word_set.sort()
        print('Word                frequency')
        for word in word_set:
            print(word + ' '*(20 - len(word)) + str(word_freq_count[word]))
