# wap to find the factorial of n.(n is the parameter)

n = 5

def calc_fact(n):
    fact = 1
    for i in range(1 , n + 1):
        fact = fact * i
    print(fact)
    
calc_fact(5)