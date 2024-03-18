collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add((1,2,3))
collection.add("apna sagar")


collection.remove(2) # {1, 3, (1, 2, 3), 'apna sagar'}
print(len(collection)) # 4
collection.clear()
print(collection) # set() empty set

