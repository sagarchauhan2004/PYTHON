i = 0
while i <= 10:
    if(i%2 == 0): # (i%2 != 0) # 2 4 6 8 10
        i += 1 
        continue # skip
    print(i)  # 1 3 5  7 9
    i =i + 1