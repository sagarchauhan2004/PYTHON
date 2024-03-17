#WAP to ask the user to enter names of their 3 favotite movies & store them in list.
movies = []


Movie1 = input("enter the 1 Movie :")
Movie2 = input("enter the 2 Movie :")
Movie3 = input("enter the 3 Movie :")

list = [Movie1 , Movie2 , Movie3]
print(list)

# or

movies.append(Movie1)
movies.append(Movie2)
movies.append(Movie3)

print(movies)