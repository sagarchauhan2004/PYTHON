food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

food2 = input("food 2 :" )
print("sweet") if food=="cake" or food == "jalebi" else print("not sweet")


# CLEVER IF
age = int(input("age : "))
vote = ("yes", "no") [age < 18]
print(vote)

sal = float(input("salary : "))
tax = sal*(0.1 , 0.2) [sal <= 50000]   #10/100   20/100
print(tax)