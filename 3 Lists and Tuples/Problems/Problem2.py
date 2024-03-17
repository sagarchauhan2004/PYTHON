# wap to check if a list contains a palindrome of elements . (hint : use copy () method)

# example : [1,2,3,2,1]

palindrome = [1,2,3,2,1]

copy_palindrome = palindrome.copy()
palindrome.reverse()

if(copy_palindrome == palindrome):
    print("palindrome")
else:
    print("not palindrome")

