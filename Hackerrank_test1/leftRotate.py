def leftRotate(lis, d):
    n=len(lis)
    d=d%n
    return lis[d:]+lis[:d]

lis=[1,2,3,4,5]
d=eval(input("Enter rotate value: "))
print("Rotated Array:",leftRotate(lis,d))