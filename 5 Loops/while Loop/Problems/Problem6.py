# wap to find the factorial of first n numbers .(for)

n_numbers = 5
i = 1
f = 1
for i in range(1 , n_numbers+1):
    f = f * i
    i = i + 1
print(f)