def Fact(n):
    if(n ==0):
        return 1
    return n * Fact(n-1)

print(Fact(5)) # 1 * 2 * 3 * 4 * 5 = 120