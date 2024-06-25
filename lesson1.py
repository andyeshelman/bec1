
# Implement a function to create a new list using list comprehension
# that contains squares of numbers from 1 to n, where n is a parameter.
# Analyze the time and space complexity of this operation.

squares = lambda n: [i*i for i in range(1,n+1)]

# O(n) in time and space

print(squares(12))

# Implement a function that has 3 parameters representing a list and 2 indices
# that will reverse a sublist within the list from index i to j (inclusive).

def subverse(arr, i, j):
    for k in range(0, (j-i+1)//2):
        arr[i + k], arr[j - k] = arr[j - k], arr[i + k]

# O(1) in space, O(j-i) in time

test = [*range(11)]
subverse(test, 3, 8)
print(test)

# Implement a function to merge two sorted lists into a single sorted list
# without using the built-in sorted function of list.sort method.

def merge_sorted(first, second):
    i = j = 0
    result = []
    while i < len(first) or j < len(second):
        if i == len(first):
            result.append(second[j])
            j += 1
        elif j == len(second):
            result.append(first[i])
            i += 1
        elif first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    return result

# O(n + k) in space and time, where n, k are the lengths of first, second

print(merge_sorted(squares(10), [11 * i for i in range(10)]))

# ====================================================================================

# Implement a function to merge two dictionaries,
# preserving the values of common keys from the second dictionary

merge_dict1 = lambda d1, d2: {**d1, **d2}

def merge_dict2(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        result[key] = value
    return result

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

print(merge_dict1(dict_1, dict_2))
print(merge_dict2(dict_1, dict_2))

# Implement a function to find the difference of two dictionaries,
# i.e., keys that are only in one of the dictionaries along with their values.

def sym_diff(d1, d2):
    result = {}
    for key, value in d1.items():
        if key not in d2:
            result[key] = value
    for key, value in d2.items():
        if key not in d1:
            result[key] = value
    return result

print(sym_diff(dict_1, dict_2))

# Implement a function to count the frequency of each unique word in a list using a dictionary.
# *Bonus* Ignore case

def word_freq1(arr):
    result = {}
    for word in arr:
        word = word.casefold()
        if word in result:
            result[word] +=1
        else:
            result[word] = 1
    return result

print(word_freq1(["The", "quick", "brown", "frog", "the", "teh", "THE", "jumped", "frog", "fox"]))

import re
from collections import Counter

def word_freq2(string):
    pat = re.compile(r"[a-z]+")
    return Counter(pat.findall(string.casefold()))

print({**word_freq2("The quick brown$$^=fox=tHe+teH+thE__be[ ]jumpin'like!!!!!!!!!frog,frog,BE,frog")})