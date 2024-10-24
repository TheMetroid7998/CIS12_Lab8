
"""11.A"""
foods = ('spaghetti', 'steak', 'pizza', 'soup')

def rev_tup(tup):
     rev = tup[::-1] # [-1:0:-1] Starts at -1, ends at 0, goes in reverse
     print(rev)

#rev_tup(foods)

"""11.B"""

keys = ['a', 'b', 'c']
values = [1, 2, 3]

#for key, value in zip(keys, values):
#    print(f"{key} -> {value}")

"""11.C"""

def mult_all(*nums):
    product = 1
    for n in nums: # each value is applied to n while in the for loop, so n will equal 2, 3, and 4 progressively
        product *= n
    print(product)

#mult_all(2, 3, 4)


"""11.11.2"""

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
t[1].append(6)
#print(t)
#d = {t: 'this tuple contains two lists'}

"""11.11.3"""

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

#print(letter_map)

def shift_word(string, shift):
    caesar_list = []
    for l in string:
        new_index = ((letter_map[f'{l}'] + shift) % 26)
        #print(new_index)
        lookup = letters[new_index]
        #print(lookup)
        caesar_list.append(lookup)
    caesar = ''.join(caesar_list)
    print(caesar)
    return caesar

#shift_word('cheer', 7)
#shift_word('melon', 16)

"""11.11.4"""

def get_value_counts(string):
    counter = {} # initialize list
    for letter in string: # iterates over each letter in the string
        counter[letter] = counter.get(letter, 0) + 1 # for each index in the string,
        # create a key/value with the letter and count and update that count as repeats are detected
    #print(counter)
    return counter

def most_freq_letters(string):
    counts = get_value_counts(string)
    #print(counts)
    frequency = sorted(counts, reverse=True)
    print(frequency)
    return frequency

#most_freq_letters('brontosaurus')

"""11.11.5"""

