# Sorting an array
# https://www.codingninjas.com/codestudio/problems/sort-0-1-2_8230695?challengeSlug=striver-sde-challenge


arr = [0, 1, 2, 2, 1, 0]
n = len(arr)

low = 0
mid = 0
high = n-1

while mid<=high:
    if arr[mid]==0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low+=1
        mid+=1

    elif arr[mid]==1:
        mid+=1 
    
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high-=1

print(arr)