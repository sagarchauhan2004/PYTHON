def find_index(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i+1] == target:
                i+=1
            return[start , i]
    return[-1,-1];

print(find_index([1,2,3,4,4,4,4] , 4))