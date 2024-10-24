
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


"""10.11.2"""

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    #print(counter)
    return counter

def get_value_counts(string):
    counter = {} # initialize list
    for letter in string: # iterates over each letter in the string
        counter[letter] = counter.get(letter, 0) + 1 # for each index in the string,
        # create a key/value with the letter and count and update that count as repeats are detected
    #print(counter)
    return counter

#value_counts('brontosaurus')
#get_value_counts('brontosaurus')

"""10.11.3"""

def has_duplicates(string):
    counter = get_value_counts(string) # use the previous function to count letters and return a dictionary
    for k, v in counter.items(): # iterate over the dictionary by key and value
        if v > 1: return True # if the value (count) is greater than 1, then it is duplicated
    return False

#print(has_duplicates('brontosaurus'))

"""10.11.4"""

def find_repeats(counter):
    counts = [] #initialize list
    for k, v in counter.items(): # iterates over dictionary counter items by key and value
        if v > 1: # if the value is over 1 (indicating a repeat/duplicate)
            counts.append(k) # append that value (letter) to the list
    return counts

"""10.11.5"""

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

def add_counters(*dicts):
    master_counts = {} # initialize the dictionary
    for d in dicts: # iterate over however many dictionaries applied
        for k, v in d.items(): # iterate by key and value over each item in the current dictionary
            master_counts[k] = master_counts.get(k, 0) + v # add to the master dict with key (letter)
            # and each count based on the supplied dictionary
    return master_counts # return the master dictionary

#print(add_counters(counter1, counter2))

"""10.11.6"""

def is_interlocking(word):
    first = word[0::2]
    #print(first)
    second = word[1::2]
    #print(second)
    print(f"'{word}' can be unpacked into '{first}' and '{second}'")

is_interlocking('schooled')