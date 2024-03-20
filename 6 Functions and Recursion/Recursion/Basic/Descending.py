def show(n):
    if(n == 0):
        return
    print(n) # 5 4 3 2 1
    show(n-1)
    
show(5)