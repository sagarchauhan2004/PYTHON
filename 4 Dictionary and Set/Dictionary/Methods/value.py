student = {
    "name" : "rohan kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 88,
        "bio" : 89
    }
}

print(student.values()) # dict_values(['rohan kumar', {'phy': 97, 'chem': 88, 'bio': 89}])

print(list(student.values())) # ['rohan kumar', {'phy': 97, 'chem': 88, 'bio': 89}]