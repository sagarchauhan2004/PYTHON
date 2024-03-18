# Sets are unordered ye print the value in jumble sentence and ignore the duplicate value


collection = {1,2,3,4 , "hello", "world"}

print(collection) # {'hello', 1, 2, 3, 4, 'world'}
print(type(collection)) # <class 'set'>


collection2 = {1,2,2,2 , "hello", "world","world" ,"4"}
print(collection2) # {'hello', 1, 2, '4', 'world'}
print(len(collection)) # 6