def leftRotate(arr, d):
    n=len(arr)
    d=d%n
    return arr[d:]+arr[:d]

arr=[1,2,3,4,5]
d=eval(input("Enter rotate value: "))
print("Rotated Array:",leftRotate(arr,d))