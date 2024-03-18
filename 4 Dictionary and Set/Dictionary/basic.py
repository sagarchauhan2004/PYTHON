info = {
    "key" : "value",
    "subjects" : ["python" , "c++", "java"],
    "name" : "sagar chauhan",
    "learning" : "python",
    "age" : 18,
    12.90 : 90.6
}

print(info) # {'key': 'value', 'subjects': ['python', 'c++', 'java'], 'name': 'sagar chauhan', 'learning': 'python', 'age': 18, 12.9: 90.6}

print(type(info)) # <class 'dict'>

print(info["subjects"])
print(info["name"])

# print(info("surname"))  # error : 'dict' object is not callable

info["name"] = "sagarwebpro" # over write
info["surname"] = "sagarwebpro chauhan"
print(info["name"]) # sagarwebpro
print(info["surname"]) # sagarwebpro chauhan

null_dict = {} # {}
print(null_dict)
null_dict["name"] = "apnasagar"
print(null_dict) # {'name': 'apnasagar'}