# write a recursive functuon to print all elements in a list

def print_list(list , idx):
    if(idx == len(list)):
        return
    print_list(list[idx])
    print_list(list,idx + 1)
    
fruit = ["mango", "litchi" , "apple" , "banana"]

print(fruit , 0)