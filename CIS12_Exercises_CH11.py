
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

mult_all(2, 3, 4)