tup = (1, 2, 3, 4, 5, 6, 8)
print(type(tup)) # <class 'tuple'>

print(tup[0])
print(tup[1])

# tup[0] = 5  it gives error tupples are immutable
 
print(tup) # (1, 2, 3, 4, 5, 6, 8)

tup2 = ("hello",) # " , " is compulsory to create a single value tupple

print(type(tup2)) # <class 'tuple'>

print(tup2) # ('hello',)


#slicing 
print(tup[1:3]) # (2, 3)