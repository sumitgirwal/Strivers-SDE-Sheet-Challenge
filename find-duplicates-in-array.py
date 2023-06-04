arr = [1, 1, 1]
n = len(arr)-1

d = dict()
for i in arr:
    if i in d.keys():
        d[i] += 1
    else: 
        d[i] = 1

for key,value in d.items():
    if value > 1 and value!=None:
        print(key)
