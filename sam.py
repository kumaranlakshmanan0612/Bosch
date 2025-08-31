
def swap_num():
    a=eval(input("Enter : "))
    b=eval(input("Enter : "))
    a=a^b
    b=a^b
    a=a^b
    print("Swapped values: a =", a, ", b =", b)

def evenOrodd():
    num = int(input("Enter a num"))
    print("Even" if num % 2 == 0 else "Odd")

def find_fact():
    n=int(input("Enter a number to find factorial: "))
    result=1
    for i in range(2, n + 1):
        result *= i
    print("Factorial of", n, "is", result)

def reverse_str():
    strr=input("Enter a string to reverse: ")
    print("Reversed string:", strr[::-1])

def vowels_consonants():
    s=input()
    s=s.lower()
    vowels=['a','e','i','o','u']
    v=0
    c=0
    for ch in s:
        if ch in vowels:
          v+=1
        else:
          c+=1
    print("Vowels:", v, "Consonants:", c)

def check_palindrome():
    s=input("Enter a string to check palindrome: ")
    cleaned=s.lower().replace(" ", "")
    print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")

def find_min_max():
    lst=eval(input("Enter a list of numbers (e.g. [1,2,3]): "))
    min_val=max_val=lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print("Minimum:", min_val, "Maximum:", max_val)

# 9. Remove Duplicates from a List
def remove_duplicates():
    lst=eval(input("Enter a list with duplicates (e.g. [1,2,2,3]): "))
    unique=[]
    for item in lst:
        if item not in unique:
            unique.append(item)
    print("List without duplicates:", unique)

# 10. Sort a List Without Using sort()
def bubble_sort():
    lst=eval(input("Enter a list to sort (e.g. [5,3,1,4]): "))
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print("Sorted list:", lst)



# --------------------------------------------------------------------------------------------------------------------
swap_num()
evenOrodd()
find_fact()
reverse_str()
vowels_consonants()
check_palindrome()
find_min_max()
remove_duplicates()
bubble_sort()

