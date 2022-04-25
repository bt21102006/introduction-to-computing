Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1   #Project1
2
3  print("solving Q1, '\n'))
4  inpnum1=int(input("enter first no."))
5  inpnum2=int(input("enter second no."))
6  inpnum3=int(input("enter third no."))
7  avg=(int(inpnum1)+int(inpum2)+int(inpum3))/3
8  print("The average of three numbers are:",(avg),'\n)

11 #Project2

12 Print("solving Q2",'n\')
13 Print('''Pleae adhere the following instructions for calculating the income tax:
14    a) All tax payers are charged a flat tax rate of 20%\
15    b) All tx payers are allowed a $10,000 standard deduction.
16    c) For each dependent, a taxpayer is allowed on additional $3000 deduction.
17    d) Gross income must be entered to the nearest penny.''')
18
19    tax_rate=0.2
20    standard_deduction=10000
21    more_deduction=3000
22    gross=int(input("please enter your gross income:"))
23    dependents=int(input("please enter no of dependents:'))
24    taxable_income=(int(gross)-int(standard_deduction)-(int(more_deduction)*int(dependents)))
25    tax=(int(taxable_income)*float(tax_rate))
26   print("your income tax value is:",(tax),"$",'\n')

29 #Project3

30 print("solving Q3",'\n')
31 print("this is your final list of semester 1 result."
32        "so please enter all the particulars sincerely")
33
34  Sid=int(input(("please enter your sid:")))
35  name=input('please enter your name")
36  gender=input("please enter your gednder")
37  course_name=input("please enter your course name:")
38  cgpa=float(input("please enter your cgpa :"))
39
40  students_list=[Sid,name,gender,course_name,cgpa]
41  print("student"+str(student_list),'\n')

43   #Project 4

44 print("solving Q4",'\n')
45 m1=int(input("enter your marks student1:"))
46 m2=int(input("enter your marks student2:"))
47 m3=int(input("enter your marks student3:"))
48 m4=int(input("enter your marks student4:"))
49 m5=int(input("enter your marks student5:"))
50
51 markslist=[m1,m2,m3,m4,m5]
52 markslist.sort()
53 print(marks list,'\n')

56 #Project5

57 # removing the elements of a given list
58 print("solving Q5",'\n')
59 color=['red','green','white','black','pink','yellow']
60 print("The provided list is",color,'\n')
61
62 # removing the fourth term and returning modified list 
63 color.pop(3)
64 print("the modified list is ", color 1=", color)
65 
66 #replacing 'black' and 'pink' with 'purple'
67 color2=['red','green','white','black','pink','yellow']
68 color2[3:5]=['purple']
69 print("the modiefied list is color 2=",color2)
