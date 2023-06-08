
def binarySearch(arr, s, e, target):
    while s<=e:
        
        mid = s+(e-s)//2

        if arr[mid]==target:
            return mid 
        elif arr[mid]>target:
            e = mid-1
        else:
            s = mid+1
    
    return -1


arr = [11, 22, 33, 44, 55, 66]
s = 0
e = len(arr)-1
target = 661

print(binarySearch(arr, s, e, target))