
"""10.A"""
from collections import defaultdict

def word_freq_counter(string):
    freq = {}
    for word in string.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    print(freq)
    return freq

def word_freq_optimized(string):
    freq = {}
    freq = defaultdict(int)
    for word in string.split():
        freq[word] += 1
    print(freq)
    return dict(freq)

#word_freq_counter('hello hello hello world')

"""10.B"""

def top_grades(dictionary):
# grades = sorted(dictionary.items(), key = lambda item: item[1], reverse=True) don't need reverse if return index is [-1]
    return sorted(dictionary.items(), key = lambda student: student[1])[-1]
"""Sorts the dict, uses a lambda key and returns with an index of -1"""

grade_book = {'Alice': 95, 'Bob': 64, 'Charlemagne': 32, 'Attila': 97}

#print(top_grades(grade_book))

"""10.C"""
from pprint import pprint

def lon_len():
    with open ('words.txt', 'r') as text:
        len_dict = {}
        for i, line in enumerate(text):
            word = line.strip()
            word_len = len(word)

            #len_dict.setdefault(len(word), []).append(word) Same thing but ~fancy~

            if word_len not in len_dict:
                len_dict[word_len] = [] # if it's not in the dictionary, create a list with a key of the length and values of the words
            len_dict[word_len].append(word) # append the words to the relevant list

            if i == 29: break # only use 30 words for testing purposes

    formatted_dict = sorted(len_dict.items()) # make output readable

    pprint(formatted_dict)
    return formatted_dict

#lon_len()


"""10.X.X"""