student = {
    "name" : "rohan kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 88,
        "bio" : 89
    }
}

print(student.keys()) # dict_keys(['name', 'subjects'])

print(list(student.keys())) # ['name', 'subjects']

print(len(list(student.keys()))) # 2