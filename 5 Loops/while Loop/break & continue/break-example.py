x = 36

num = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(num):
    if(num[i]== x):
        print("found at index :",i)
        break
    else:
        print("finding...")
    i = i + 1

print("end of loop")