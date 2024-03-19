# wap to print the elements of a list in a single line . (list is the parameter)



cities = ["delji","gurgaon","noida","pune","mumbai","chennai"]
heros = ["thor","ironman","captain america","shaktiman"]


def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item , end=" ")
        
print_list(heros)