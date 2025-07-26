# def fact(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     print(fact)
# fact(6)

# def fact(a):
    
#     if a==1 or a==0:
#         return 1
   
#     return a*fact(a-1)

# print(fact(6))

# def permutation(a,r):
#     return fact(a)//fact(a-r)
# print(permutation(5,2))


# def combi(a,r):
#     return fact(a)//(fact(a-r)*fact(r))
# print(combi(5,2))

# def sum(n):
#     if n==1:
#         return 1 
#     return n+sum(n-1)
# print(sum(5))


#facrorial using recursion
# def fact(a):
    
#     if a==1 or a==0:
#         return 1
   
#     return a*fact(a-1)

# print(fact(6))


#file I/O

# file_name=open("demo.txt","r")
# data=file_name.read(5) # for reading only one line we use .readline
# print(data)
# file_name.close()


# file_name=open("demo.txt","w")
# data=file_name.write("abcs,mkcbn") 

# print(data)
# file_name.close()

# # import os
# os.rename("demo.txt","test.txt")

# file_name=open("practice.txt","w")
# file_name.write("Hi everyone.\nWe are learning File Handling I/O\nusing python\ni like programming in python")
# file_name=open("practice.txt","r")
# data=file_name.read()
# data=data.replace("python","javascript")
# file_name=open("practice.txt","w")
# file_name.write(data)
# file_name.close()


#lamda function

#lamda is short anonymous function
# sum=lambda x,y:x+y
# print(sum(2,5))

# sq=lambda x:x*x
# print(sq(9))


# lst=list(map(int,input("enter a list:").split()))
# sq=list(map(lambda x:x*2,lst))
# print(sq)


#Exception handling

# try:
#     a = 2
#     b = 0
#     c = a / b
#     print(c)
# except Exception as e:
#     print(e)

#random password generator
import string
import random
ps=""
a=string.printable
# n=int(input("enter the size:"))
for i in range(1,9):
    d=random.choice(a)
    ps+=d
print(ps)