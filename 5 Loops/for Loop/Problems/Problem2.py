# search for a number x in this tuple using loop:  (1,4,9,16,25,36,49,64,81,100)

tup =  (1,4,9,16,25,36,49,64,81,100)
x = 36

index = 0
for numbers in tup:
    if(numbers == x):
        print(numbers, "found at index :",index)
    index = index + 1
   