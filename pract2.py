from collections import Counter
import sys

def count_frequency(lst):
    return dict(Counter(lst))

def merge_dicts(d1, d2):
    return {**d1, **d2}

def second_largest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort(reverse=True)
    return unique_lst[1]

def sum_kwargs(**kwargs):
    return sum(kwargs.values())

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return None

def read_args():
    return sys.argv[1:]

def count_words_in_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return len(text.split())

print("Frequency Count:", count_frequency([1, 2, 2, 3, 3, 3, 4]))
print("Merged Dictionaries:", merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print("Second Largest Number:", second_largest([5, 2, 9, 1, 5, 6]))
print("Sum of kwargs:", sum_kwargs(a=10, b=20, c=30))
print("Common Elements:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print("Primes in Range 10-30:", find_primes(10, 30))
print("Are 'listen' and 'silent' anagrams?:", are_anagrams("listen", "silent"))
print("Calculator (10 / 2):", calculator(10, 2, '/'))
print("Command-line Arguments:", read_args())
