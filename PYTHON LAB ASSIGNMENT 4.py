Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q.1
>>> marks=float(input("Enter Marks: "))
Enter Marks: if(marks<25):
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'if(marks<25):'
>>>     print(" Grade F ")
  File "<stdin>", line 1
    print(" Grade F ")
IndentationError: unexpected indent
>>> elif(marks>=25 and marks<45):
  File "<stdin>", line 1
    elif(marks>=25 and marks<45):
    ^^^^
SyntaxError: invalid syntax
>>>     print(" Grade E ")
  File "<stdin>", line 1
    print(" Grade E ")
IndentationError: unexpected indent
>>> elif(marks>=45 and marks<50):
  File "<stdin>", line 1
    elif(marks>=45 and marks<50):
    ^^^^
SyntaxError: invalid syntax
>>>     print(" Grade D ")
  File "<stdin>", line 1
    print(" Grade D ")
IndentationError: unexpected indent
>>> elif(marks>=50 and marks<60):
  File "<stdin>", line 1
    elif(marks>=50 and marks<60):
    ^^^^
SyntaxError: invalid syntax
>>>     print(" Grade C ")
  File "<stdin>", line 1
    print(" Grade C ")
IndentationError: unexpected indent
>>> elif(marks>=60 and marks<80):
  File "<stdin>", line 1
    elif(marks>=60 and marks<80):
    ^^^^
SyntaxError: invalid syntax
>>>     print(" Grade B ")
  File "<stdin>", line 1
    print(" Grade B ")
IndentationError: unexpected indent
>>> elif(marks>=80 ):
  File "<stdin>", line 1
    elif(marks>=80 ):
    ^^^^
SyntaxError: invalid syntax
>>>     print(" Grade A ")
  File "<stdin>", line 1
    print(" Grade A ")
IndentationError: unexpected indent
>>> else:
  File "<stdin>", line 1
    else:
    ^^^^
SyntaxError: invalid syntax
>>>     print(" ERROR ")
  File "<stdin>", line 1
    print(" ERROR ")
IndentationError: unexpected indent
>>>
>>>
>>> #Q.2
>>> year = int(input("Enter a year: "))
Enter a year:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> if year % 4 == 0 :
...     print(year ,"is a Leap Year")
... elif year % 100 == 0 :
...     print(year ,"is not a Leap Year")
... elif year % 400 == 0 :
...     print(year ,"is a Leap Year")
... else :
...     print(" ERROR ")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'year' is not defined
>>>
>>> #Q.3
>>> import random
>>> for i in range(10):
...     num1 = random.randint(1,10)
...     num2 = random.randint(1,10)
...     print(f"Question {i+1}:",end="")
...     user_output = int(input(f"{num1}X{num2}="))
...     if user_output == (num1*num2):
...         print("Right!")
...     else:
...         print(f"Wrong.The right answer is {num1*num2}.")
...
Question 1:9X2=
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> #Q.4
>>> x=200
>>> for candies in range(x):
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>     if candies % 5 == 2:
  File "<stdin>", line 1
    if candies % 5 == 2:
IndentationError: unexpected indent
>>>        if candies % 6 == 3:
  File "<stdin>", line 1
    if candies % 6 == 3:
IndentationError: unexpected indent
>>>           if candies % 7 == 2:
  File "<stdin>", line 1
    if candies % 7 == 2:
IndentationError: unexpected indent
>>>              print(candies, 'candies are in the bowl!')
  File "<stdin>", line 1
    print(candies, 'candies are in the bowl!')
IndentationError: unexpected indent
>>>

