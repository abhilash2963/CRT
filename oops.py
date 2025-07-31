# class Student():
#     name ="Abhi"
#     college="KPRIT"
#     def __init__(self):#created by default and executed just after object is created 
#         print("student object created")


#     def hello(self):
#         print(self)


# s1=Student()  #constructor
# print(s1.name)
# # print(s1.name)
# # print(s1.college)



#     def __init__(self,name):#created by default and executed just after object is created 
#          print("student object created")
#          self.name=name
    
# s1=Student("abhi")
# print(s1.name)
# s2=Student("raju")
# print(s2.name)



# class Student():
#     def __init__(self,s1,s2,s3,m1,m2,m3):
#         self.s1=s1
#         self.s2=s2
#         self.s3=s3
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         avg=(self.m1+self.m2+self.m3)//3
#         print(avg)

# s=Student("a","b","c",70,85,92)
# s.avg()

#practice 2

# class circle():
#     def __init__(self,radi):
#         self.radi=radi
#     def area(self):
#         area=(3.14)*self.radi**2
#         print(area)
#     def perimeter(self):
#         peri=2*(3.14)*self.radi
#         print(peri)
    
      
# c1=circle(7)
# c1.area()
# c1.perimeter()
     

#static methodes

# class student():
#     @staticmethod
#     def hello():
#         print("hello")
# s1=student()
# s1.hello()


#practice test 2

class acc:
    def __init__(self,accno,bal):
        self.accno=accno
        self.bal=bal
    def debit(self,debamount):
        if self.bal>=debamount:
            self.bal=self.bal-debamount
            print(f"rs.{debamount} debited and balance is{self.bal}")
        else:
            print("insufficient bal")
            

    def credit(self,credamount):
        self.bal=self.bal+credamount
    def displayamount(self):
        print(self.bal)

a1=acc("acc1234",5000)
a1.debit(1000)
a1.credit(2000)

a1.displayamount()
