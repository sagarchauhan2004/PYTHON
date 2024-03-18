# wap to enter marks of 3 subjects from the user and store them in a dictionary. Strat wuth a empt dictionary & add one by one . use subject name as key & marks as value

 
subject1 =  input("enter the phy marks :")
subject2 =  input("enter the chem marks :")
subject3 =  input("enter the bio marks :")

dect = {
    subject1 , subject2 ,subject3
}
print(dect)

#or

marks = {}
x = int(input("enter phy :"))
marks.update({"phy" : x})

x = int(input("enter chem :"))
marks.update({"chem" : x})

x = int(input("enter bio:"))
marks.update({"bio" : x})

print(marks)