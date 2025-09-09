def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top=stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

try:
    paran = input("Enter the brackets: ")
    if is_valid(paran):
        print("Brackets are balanced")
    else:
        print("Brackets are NOT balanced")
except KeyboardInterrupt:
    print("Input cancelled by user.")