#dictionaty

# mydict={
#     "name": "abhilash",
#     "age": 20,
#     "is student": True
# }

# print(mydict)

#declaring same dictionary again can over ride the privious one entirley

#dict modification

# mydict["name"]="abhi"
# print(mydict)

#insertion

# mydict["ok"]="nothing"  #this is not the corrct way
# print(mydict)


# #nested dictionary
# dict={
# "nsme":"abhi",
# "marks":{
#     "math":90,
#     "physics":89
# }
# }

#problem 1

# mydict={
#     "table":
#     [
#         "a pice of furneture","list of facts and figures"
#     ],
#     "cat": "a small animal"
    

#     }
# print(mydict.items())

#problem2 

# user_marks={
#     "math": 90,
#     "physics": 80,
#     "chemistry": 79

# }

# dict_marks={}

# n=int(input("enter size: "))
# for i in range(1,n+1):
#     key=input(f"enter the subject{i}:")
#     value=int(input(f"enter the marks {key}:"))
#     dict_marks.update({key:value})

# print(dict_marks)

# dict_squares={
# }
# for i in range(1,11):
#     key=i
#     value=i*i
#     dict_squares.update({key:value})

# print(dict_squares)


#functions.......

# def length(lst):
#     return (len(lst))
# print(length([653,57,46,67,78]))
# print(length([7,66,8,9,0,0,66]))

# def print_ele(my_lst):
#     for i in my_lst:
#         print(i,end=" ")
# print_ele([2,3,4,5,6])


# def ustoinr(us):
#     print(f"indian rupees ={us*85}")

# ustoinr(1000)

