Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Question 1
# Write a program to take a number as input and convert it into its binary equivalent.

number = int(input("Enter any number: "))
print("binary equivalent of the number is",bin(number)[2:])


# Question 2
# Write an interactive Python calculator program. The program should allow the user
# to type a mathematical expression, and then print the value of the expression.

expression = input("Enter your expression: ")
print(eval(expression))


# Question 3
import math
# (a)
print((3+4)*(5))
# (b)
n= float(input("Enter the value of n: "))
print(n*(n-1)/2)
# (c)
r1=float(input("Enter the value of r1: "))
print(4*math.pi*r1**2)
# (d)
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
r2=float(input("Enter the value of r2: "))
print(math.sqrt(r2*(math.cos(a)*2) + r2(math.sin(b)**2)))
# (e)
x1=float(input("Enter the value of x1: "))
x2=float(input("Enter the value of x2: "))
y1=float(input("Enter the value of y1: "))
y2=float(input("Enter the value of y2: "))
print((y2-y1)/(x2-x1))

# Question 4
# Show the sequence of numbers that would be generated by each of the following
# range expressions.

# (a)
for i in range(5):
    print(i,end=" ")
print()
# (b)
for i in range(3,10):
    print(i,end=" ")
print()
# (c)
for i in range(4,13,3):
    print(i,end=" ")
print()
# (d)
for i in range(15,5,-2):
    print(i,end=" ")
print()
# (e)
for i in range(5,3):
    print(i,end=" ")
print()


# Question 5
h= int(input("enter number of hydrogen atoms : "))
c= int(input("enter number of carbon atoms : "))
o= int(input("enter number of oxygen atoms : "))
d=(h*1.00794)+(c*12.0107)+(o*15.9994)
print("combined molecular weight of all atoms is :",d)