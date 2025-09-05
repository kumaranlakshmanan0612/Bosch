def getMax(operations):
    stack = []
    max_stack = []
    result = []
 
    for op in operations:
        parts = op.split()
        if parts[0] == "1":  # push
            x = int(parts[1])
            stack.append(x)
            if not max_stack:
                max_stack.append(x)
            else:
                max_stack.append(max(x, max_stack[-1]))
        elif parts[0] == "2":  # pop
            stack.pop()
            max_stack.pop()
        else:  # parts[0] == "3"
            result.append(max_stack[-1])
    return result
 
 
if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    n = int(input().strip())
    ops = [input().strip() for _ in range(n)]
 
    res = getMax(ops)
 
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()