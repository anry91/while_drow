size_b = int(input("Enter big lenght: "))
size_s = int(input("Enter small lenght: "))
lenght = size_b * size_s
direction = input("What lenght must to be horizontally b or s: ")
n = 1
if direction == "b":   
    while n <=lenght :
        print("+", end=" ")
        if n % size_b == 0:
          print()

        n+=1
else:
    while n <=lenght :
        print("+", end=" ")
        if n % size_s == 0:
          print()

        n+=1