Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Project1

print("Solving Q1:", ' \n')
fantastic = input("Please Enter Any String:")
print(fantastic)

#[a] (size of string)
print("a. Size of string is: ", len(fantastic))

#[b] (reverse string)
fantastic1 = fantastic[::-1] # we can also type fantastic[0:35:-1]
print("b. The reversed string is: ", fantastic1)

#[c] (slicing string)
c = slice(10, 26)
print("c. String after slicing: ", fantastic[c])

#[d] (replace substring)
d = fantastic.replace('a case sensitive', 'object oriented')
print("d. Replacing substring: ", d)

#[e] (finding index of substring)
e = fantastic.index('a') # we can also type fantastic.find('a')
print("e. The index of 'a' is: ", e)

#[f] (removing spaces from the string)
f = fantastic.replace(' ','')
print("f. Removing white spaces: ", f, end="\n")

#Project2

print("Solving Q2:", '\n')
Name='ABC'
SID=21102053
Department='XYZ'
CGPA=9.9
print("Hey, %s Here! \nMy SID is %d \nI am from %s department and my CGPA is %f." % (Name, SID, Department, CGPA), end='\n')

#Project3

print("Solving Q3:", '\n')
a=56
b=10
print("a & b=", (a & b))
print("a | b=", (a | b))
print("a ^ b=", (a ^ b))
print("Left shift both a and b with 2 bits : a=",a<<2, "b=", b<<2)
print("Right shift a with 2 bits and b with 4 bits : a=", a>>2, "b=", b>>4, end='\n')

#Project4

print("Solving Q4:", '\n')
food = str(input("Enter the string:"))
print(food)
word = "name"

if word in food:
    print('Yes')
else:
    print("No")
print(end='\n')

#Project5

print("Solving Q5:", '\n')
side_a = int(input("Enter the 1st side of the triangle : "))
side_b = int(input("Enter the 2nd side of the triangle : "))
side_c = int(input("Enter the 3rd side of the triangle : "))
if side_a > side_b + side_c and side_b > side_a + side_c and side_c > side_a + side_b:
    print('Yes')
else:
    print('No')
print(end='\n')

#Project6

print("Solving Q6:", '\n')

inpnum1 = int(input("Enter first number:"))
inpnum2 = int(input("Enter second number:"))

num = inpnum1 ^ inpnum2

i = 0
while (num != 0):
    num = num & (num - 1)
    i = i + 1
print("Num of bits needed to be flipped to convert a to b is:", i)