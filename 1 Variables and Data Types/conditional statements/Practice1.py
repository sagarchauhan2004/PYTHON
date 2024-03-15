A = int(input("A : "))
G = input("Male/Female : ")

if((A ==1 or A ==2) and G == "M"):
    print("fee is 100")
elif((A ==3 or A ==3) and G == "F"):
    print("fee is 200")
elif(A ==5 and G == "M"):
    print("fee is 500")    
else:
    print("no fee")    