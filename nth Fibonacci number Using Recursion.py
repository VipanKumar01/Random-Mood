# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

"""
Write a program in python and create a  recursive code to compute the nth Fibonacci number?
"""

def Fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)
    

num = int(input('Enter Any No. to Conpute Fibonacci Series : '))
data = []

for i in range(1,num+1):
    result = Fibo(i)
    data.append(result)

print(f'Fibonacci Series of the {num} is :',data)

# --Happy Code --
