# Pattern Printing

# input = integer n
# Boolean = True or False

# True n = no of row
# *
# **
# ***
# ****
#
# False n = no of row
# ****
# ***
# **
# *

# print("Let's print a pattern of *")
# print("Enter a number to get star pattern : ",end="")
# inp = int(input())
#
#
# if inp==1:
#     print("*")
# elif inp==2:
#     print("*")
#     print("**")
# elif inp==3:
#     print("*")
#     print("**")
#     print("***")
# elif inp==4:
#     print("*")
#     print("**")
#     print("***")
#     print("****")
# else:
#     print("You have entered maximum numbers.")


print("How many row you want to print * pattern")
one = int(input())
print("Type 1 or 0 ")
two = int(input())
new = bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new == False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
