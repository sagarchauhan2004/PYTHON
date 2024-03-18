student = {
    "name" : "rohan kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 88,
        "bio" : 89
    }
}

print(student.items()) # dict_items([('name', 'rohan kumar'), ('subjects', {'phy': 97, 'chem': 88, 'bio': 89})]) # (key , val)

print(list(student.items())) # [('name', 'rohan kumar'), ('subjects', {'phy': 97, 'chem': 88, 'bio': 89})]

pairs = list(student.items())
print(pairs[0]) # ('name', 'rohan kumar')

print(pairs[1]) # ('subjects', {'phy': 97, 'chem': 88, 'bio': 89})