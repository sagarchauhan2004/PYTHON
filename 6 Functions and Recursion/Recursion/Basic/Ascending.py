def show(n):
    if(n == 0):
        return
    show(n-1)
    print(n) # 1 2 3 4 5
    
show(5)