from os import system

system("cls")
#. . . . +                4   1
#. . . + + +              3   3 
#. . + + + + +            2   5
#. + + + + + + +          1   7
#+ + + + + + + + +        0   9


#
number = int(input("enter number: "))

n=0 
while n<number:
    print(". " * (number-1-n), "+ " * (2*n+1))
    n+=1