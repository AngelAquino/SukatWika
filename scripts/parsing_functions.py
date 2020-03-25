'''
UP CIDS-ERP and UP DSP
"Mother Tongue-Based Multilingual Education Literacy Test Package"

Parsing Functions
'''

def text2wlist(text_address):
    """Returns a single list of words in the text file."""
    # import unidecode
    import re, string

    wlist = []

    with open(text_address, 'r') as text_file:
        txt = text_file.read()

        # convert to lowercase ASCII estimate
        # txt = unidecode.unidecode(txt).lower()
        txt = txt.lower()

        # remove non-alphanumerics except '-' and whitespace
        txt = re.sub('[^A-Za-z0-9\s-]+', '', txt)
        txt = re.sub('--+', '', txt)

        # replace consecutive whitespace with single space
        txt = re.sub('\s+', ' ', txt)

        wlist += txt.split()

    return wlist


def text2pslist(text_address):
    """Returns lists containing whole sentences in each line (paragraph) of the text file."""
    import re, string

    parlist = []

    with open(text_address, 'r') as text_file:
        for line in text_file:
            if line.strip() != '':
                senlist = [str.strip() for str in re.split('\.|\?|!', re.sub('[^A-Za-z0-9\s\.\?!-]+', '', line)) if str.strip() != '']
                parlist.append(senlist)

    return parlist


def word2syll_tgl(word):
    """Input: word (single string). Output: syllables (list of strings)."""

    vowel_list = ['a', 'e', 'i', 'o', 'u']
    nasal_list = ['m', 'n']
    nasal_digraph_list = ['bl', 'br', 'pl', 'pr', 'dr', 'tr']
    digraph_list = ['ng']

    syll_list = []
    curr_syll = ''
    vowel_flag = False
    idx = 0

    while idx < len(word):
        c = word[idx]

        if c == '-':
            syll_list.append(curr_syll)
            curr_syll = ''
            vowel_flag = False
            idx += 1
            continue

        if vowel_flag == False:
            curr_syll += c
            if c in vowel_list:
                vowel_flag = True
            idx += 1
            continue

        if c in vowel_list:
            syll_list.append(curr_syll)
            curr_syll = c
            vowel_flag = True
            idx += 1
            continue

        i = 1
        word_final = True
        while idx + i < len(word):
            if word[idx + i] in vowel_list:
                word_final = False
                break
            if word[idx + i] == '-':    # hyphen divisions as separate 'words'
                break
            i += 1

        if word_final == True:
            curr_syll += c
            idx += 1
            continue

        if i >= 3:
            if c in nasal_list and word[idx+1:idx+3] in nasal_digraph_list:
                syll_list.append(curr_syll + c)
                curr_syll = ''
                vowel_flag = False
                idx += 1
            else:
                syll_list.append(curr_syll + word[idx:idx+2])
                curr_syll = ''
                vowel_flag = False
                idx += 2

        elif i == 2:
            if word[idx:idx+2] in digraph_list:
                syll_list.append(curr_syll)
                curr_syll = c
                vowel_flag = False
                idx += 1
            else:
                syll_list.append(curr_syll + c)
                curr_syll = ''
                vowel_flag = False
                idx += 1

        else:
            syll_list.append(curr_syll)
            curr_syll = c
            vowel_flag = False
            idx += 1

    if len(curr_syll):  # if syllable is not empty
        syll_list.append(curr_syll)

    return syll_list


def syll2phon_tgl(syll):
    """Input: word (single string). Output: phonemes (list of strings)."""

    digraph_list = ['ng']
    diphthong_list = ['ay', 'aw', 'ey', 'iw', 'oy', 'ow', 'uy']

    phon_list = []
    idx = 0

    while idx < len(syll):
        if idx + 1 < len(syll) and syll[idx:idx+2] in digraph_list + diphthong_list:
            phon_list.append(syll[idx:idx+2])
            idx += 2
        else:
            phon_list.append(syll[idx])
            idx += 1

    return phon_list


def word2phon_tgl(word):
    if word == 'ng':
        return ['n', 'a', 'ng']

    syll_list = word2syll_tgl(word)
    phon_list = []
    for syll in syll_list:
        phon_list += syll2phon_tgl(syll)

    return phon_list


def word2syll_ilk(word):
    """Input: word (single string). Output: syllables (list of strings)."""

    vowel_list = ['a', 'e', 'i', 'o', 'u']
    nasal_list = ['m', 'n']
    nasal_digraph_list = ['bl', 'br', 'pl', 'pr', 'dr', 'tr']
    digraph_list = ['ng']
    diphthong_list = ['ia', 'ie', 'io', 'iu', 'ea', 'eo', 'eu', 'oa', 'oe', 'ua', 'ue', 'uio']

    syll_list = []
    curr_syll = ''
    vowel_flag = False
    diphthong_flag = False
    idx = 0

    while idx < len(word):
        c = word[idx]

        if c == '-':
            syll_list.append(curr_syll)
            curr_syll = ''
            vowel_flag = False
            idx += 1
            continue

        if vowel_flag == False:
            curr_syll += c
            if c in vowel_list:
                if diphthong_flag == False and idx + 1 < len(word) and word[idx:idx+2] in diphthong_list:
                    diphthong_flag = True
                elif diphthong_flag == False and idx + 2 < len(word) and word[idx:idx+3] in diphthong_list:
                    diphthong_flag = True
                    curr_syll += word[idx+1]
                    idx += 1
                else:
                    diphthong_flag = False
                    vowel_flag = True
            idx += 1
            continue

        if c in vowel_list:
            syll_list.append(curr_syll)
            curr_syll = c
            vowel_flag = True
            idx += 1
            continue

        i = 1
        word_final = True
        while idx + i < len(word):
            if word[idx + i] in vowel_list:
                word_final = False
                break
            if word[idx + i] == '-':    # hyphen divisions as separate 'words'
                break
            i += 1

        if word_final == True:
            curr_syll += c
            idx += 1
            continue

        if i >= 3:
            if c in nasal_list and word[idx+1:idx+3] in nasal_digraph_list:
                syll_list.append(curr_syll + c)
                curr_syll = ''
                vowel_flag = False
                idx += 1
            else:
                syll_list.append(curr_syll + word[idx:idx+2])
                curr_syll = ''
                vowel_flag = False
                idx += 2

        elif i == 2:
            if word[idx:idx+2] in digraph_list:
                syll_list.append(curr_syll)
                curr_syll = c
                vowel_flag = False
                idx += 1
            else:
                syll_list.append(curr_syll + c)
                curr_syll = ''
                vowel_flag = False
                idx += 1

        else:
            syll_list.append(curr_syll)
            curr_syll = c
            vowel_flag = False
            idx += 1

    if len(curr_syll):  # if syllable is not empty
        syll_list.append(curr_syll)

    return syll_list


def syll2phon_ilk(syll):
    """Input: word (single string). Output: phonemes (list of strings)."""

    digraph_list = ['ng']
    diphthong_list = ['ia', 'ie', 'io', 'iu', 'ea', 'eo', 'eu', 'ya', 'ye', 'yo', 'yu', 'oa', 'oe', 'ua', 'ue', 'uio', 'wa', 'we', 'wi']

    phon_list = []
    idx = 0

    while idx < len(syll):
        if idx + 2 < len(syll) and syll[idx:idx+3] in digraph_list + diphthong_list:
            phon_list.append(syll[idx:idx+3])
            idx += 3
        elif idx + 1 < len(syll) and syll[idx:idx+2] in digraph_list + diphthong_list:
            phon_list.append(syll[idx:idx+2])
            idx += 2
        else:
            phon_list.append(syll[idx])
            idx += 1

    return phon_list


def word2phon_ilk(word):
    if word == 'ng':
        return ['n', 'a', 'ng']

    syll_list = word2syll_ilk(word)
    phon_list = []
    for syll in syll_list:
        phon_list += syll2phon_ilk(syll)

    return phon_list


def phon_lookup_eng(phon_lookup_address):
    """Creates a Python dictionary from a CMUdict-formatted pronunciation dictionary file."""
    phon_lookup = dict()

    with open(phon_lookup_address, 'r') as dict_file:
        for line in dict_file:
            ls = line.lower().split()

            phon_lookup[ls[0]] = ls[1:]

    return phon_lookup


def word2phon_eng(word, phon_lookup):
    """Input: word (single string). Output: phonemes (list of strings). Uses ARPABET phoneme notation."""

    if word in phon_lookup.keys():
        return phon_lookup[word]
    else:
        return []

def word2phonogram_eng(word, phon_list):

    pgram_list = []
    word_idx, phon_idx, last_word_idx, last_phon_idx = 0, 0, 0, 0

    pgram_dict = {  'aa': ['a', 'o'],
                    'ae': ['a'],
                    'ah': ['a', 'e', 'i', 'o', 'u'],
                    'ao': ['o', 'aw', 'au'],
                    'aw': ['ou', 'ow'],
                    'ay': ['i', 'igh', 'ie', 'y'],  # (li) tag, i-e, y-e
                    'eh': ['e', 'ea', 'ai'],
                    'er': ['er', 'ir', 'ur', 'ar', 'or', 'ear'],
                    'ey': ['a', 'ai', 'ay', 'eigh', 'ei', 'ey', 'ea'], # (la) tag
                    'ih': ['i', 'y'],
                    'iy': ['e', 'ee', 'ea', 'ie', 'y', 'ey'], # (le) tag, e-e
                    'ow': ['o', 'oa', 'ow', 'oe'], # (lo) tag
                    'oy': ['oi', 'oy'],
                    'uh': ['u', 'oo'],
                    'uw': ['oo', 'ew', 'ou', 'ue', 'u', 'ui'], # (lu) tag
                    'b' : ['b'],
                    'ch': ['ch', 'tch'],
                    'd' : ['d'],
                    'dh': ['th'],
                    'f' : ['f', 'ph'],
                    'g' : ['g'],
                    'hh': ['h'],
                    'jh': ['j', 'g', 'dg'],
                    'k' : ['c', 'k', 'ck'],
                    'l' : ['l'],
                    'm' : ['m'],
                    'n' : ['n', 'kn'],
                    'ng': ['ng'],
                    'p' : ['p'],
                    'r' : ['r', 'wr'],
                    's' : ['s', 'c'],
                    'sh': ['sh', 'ch', 'ssi', 'ti', 'si', 'ci'],
                    't' : ['t'],
                    'th': ['th'],
                    'v' : ['v'],
                    'w' : ['w'],
                    'y' : ['y', 'i', 'j'],
                    'z' : ['z', 's'],
                    'zh': ['s', 'g', 'j'],
                    'kw': ['qu'],
                    'yuw': ['u', 'ew', 'ue', 'eu']}

    while word_idx != len(word) and phon_idx != len(phon_list):
        phon_found = False

        for i in range(min(4, len(word) - word_idx), 0, -1):
            if phon_idx+1 < len(phon_list) and phon_list[phon_idx] + phon_list[phon_idx+1] == 'kw' and word[word_idx:word_idx+i] in pgram_dict['kw']:
                pgram_list.append(word[word_idx:word_idx+i] + '(kw)')
                phon_found = True
                phon_idx += 2
                word_idx += i
                break

            elif phon_idx+1 < len(phon_list) and phon_list[phon_idx] + phon_list[phon_idx+1] == 'yuw' and word[word_idx:word_idx+i] in pgram_dict['yuw']:
                pgram_list.append(word[word_idx:word_idx+i] + '(yuw)')
                phon_found = True
                phon_idx += 2
                word_idx += i
                break

            elif word[word_idx:word_idx + i] in pgram_dict[phon_list[phon_idx]]:
                pgram_list.append(word[word_idx:word_idx+i] + '(' + phon_list[phon_idx] + ')')
                phon_found = True
                phon_idx += 1
                word_idx += i
                break

        if phon_found == True:
            last_word_idx = word_idx
            last_phon_idx = phon_idx
        elif phon_found == False:
            if word_idx+1 == len(word): # move to next phone
                # print(phon_list[phon_idx], 'not found; current list:', pgram_list)
                phon_idx = last_phon_idx + 1
                word_idx = last_word_idx
                last_phon_idx += 1
            else:
                word_idx += 1

    return pgram_list

def get_phon_keywords(phon_keyword_address):
    """Creates a Python dictionary of keywords from a phoneme-keyword CSV file."""
    phon_keywords = dict()

    with open(phon_keyword_address, 'r') as csv_file:
        for line in csv_file:
            if line.strip() != '':
                ls = line.strip().split(',')
                phon_keywords[ls[0]] = ls[1]

    return phon_keywords
