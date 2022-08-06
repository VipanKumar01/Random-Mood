# Name = Vipan Kumar
# GitHub user name = @VipanKumar01
"""
Write a program in python to create a recursive code to find the sum of all elements of a list?
"""

def Total(alist,n):
    if n == 0:
        return 0
    else:
        return alist[n-1] + Total(alist,n-1)
    
alist = eval(input("Enter list elements(numerals Comma Separated ): "))
result = Total(alist, len(alist))

print("The sum of the list ",alist," is ---> ",result)

# -- Happy Code --
