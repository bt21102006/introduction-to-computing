Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

Question 1
def is_perfect_number(n):
    sum=0
    sum_all=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            sum_all+=i
    sum2=(sum_all+n)//2        
    return sum==n , sum2==n
p=int(input())
print(is_perfect_number(p))
28
(True, True)
Question 2
def is_palindrome(n):
    
    new=word[::-1]
    return word==new
word=input()
is_palindrome(word)
ketan
False
Question 3
from math import factorial

def pascal_tri(numRows):
  '''Print Pascal's triangle with numRows.'''
  for i in range(numRows):
    # loop to get leading spaces
    for j in range(numRows-i+1):
        print(end=" ")
    
    # loop to get elements of row i
    for j in range(i+1):
		  # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	 # print each row in a new line
    print("\n")

pascal_tri(5)
      1 

     1 1 

    1 2 1 

   1 3 3 1 

  1 4 6 4 1 

Question 4
def ispangram(string):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha :
        if i not in string.lower():
            return False
    return True
string=input()
print(ispangram(string))
akhdb
False
Question 5
def hyphen(sent):
    words=sent.split("-")
    word=sorted(words)
    return "-".join(word)
n=input()
hyphen(n)
violet-yellow-alladin-ketan-pec-red-papaya
'alladin-ketan-papaya-pec-red-violet-yellow'
Question 6
def student_data(student_id,**kwargs):
    print("Student ID:",student_id)
    if "student_name" in kwargs:
        print("Student name :",kwargs['student_name'])
    if "student_class" in kwargs :
        print("Student class :",kwargs['student_class'])
        

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')

student_data(student_id='SV12', student_name='Jean Garner')
Student ID: SV12
Student name : Jean Garner
Student class : V
Student ID: SV12
Student name : Jean Garner
Question 7
class Student:
    pass
class Marks:
    pass
ketan=Student()
a_grade=Marks()
print("To check whether they are instances of said classes or not:")
print(isinstance(ketan,Student))
print(isinstance(ketan,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))
To check whether they are instances of said classes or not:
True
False
True
False

To check whether the said classes are subclasses of the built-in object class or not:
True
True
Question 8
class solution:
    def sumthree(self,nums):
        nums=sorted(nums)
        result=[]
        i=0
        while i < len(nums)-2 :
            j , k = i+1 , len(nums)-1
            while j<k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] >0 :
                    k-=1
                else :
                    result.append([nums[i] ,nums[j] ,nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j -1]:
                        j+=1
                    while j<k and nums[k]== nums[k+1] :
                        k-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
        return result
print(solution().sumthree([-25, -10, -7, -3, 2, 4, 8, 10]))
[[-10, 2, 8], [-7, -3, 10]]
Question 9
class sol:
    def validity(self,str1):
        accum=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accum.append(i)
            elif len(accum)==0 or parentheses[accum.pop()]!=i:
                return False
        return len(accum)==0
print(sol().validity("((("))
False