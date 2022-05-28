# def greeting(name,age):
#     year = 2022-age
#     return f"Hello {name} you were born in {year}"

# greeting("suzan",21) 
# greeting("Effence",21)
# greeting(21,"Effence")

# greeting(name="suzan",age=21)
# greeting(age=21,name="Effence")

# def my_country(country="Uganda",student="susan"):
#     return f"Hello {student} you are from {country}"

# my_country()
# my_country(country="Rwanda",student="verite")

# def greet_multiple(*names):
#     for name in names:
#         print(f"Hello {name}")

# greet_multiple ("susan","Effense","Brenda")
# greet_multiple  ("susan","Effense","Brenda","Queenter","Grace") 


#write a function that accepts any 
# number of integers and returns the sum of all of them
# def add(*numbers):
#     for number in numbers:
#         sum+=number
#     return sum

# def multiply(*numbers):
#     for number in numbers:
#         multiply*=number
#     return multiply


# from collections import Counter
# from unicodedata import name


# def greet_multiple(**kwargs):
#     print(kwargs) 
#     print(kwargs.keys())
#     print(kwargs.values())

# greet_multiple(name="Queenter")
# greet_multiple(name="Queenter",age=24)
# greet_multiple(name="Queenter",age=24,country="Kenya") 
# greet_multiple()

# def greet_multiple(**kwargs):
#     keys = kwargs.keys()
#     if "country" in keys:
#         print (f"Hello {kwargs['name']}")
#         print (f"Hello {kwargs['name']}" ) 
#         print (f"Hello {kwargs['name']}")

#     elif"age" in  keys:
#            year = 2022 - kwargs ['age']
#            print (f"hello {kwargs['name']} you were born {year}") 

#     elif not kwargs:
#      print (f"Hello anonymous")

# greet_multiple(name="Queenter",country="Kenya")
# greet_multiple(name="Queenter",age=24,school="Akirachix")
# greet_multiple()  


# def sum_and_greet(*args,**kwargs):
#     sum = 0
#     for num in args:
#         sum +=num

#     keys = kwargs.kys()
#     if "name" in keys:
#         print(f"hello {kwargs[name]},the answer is {sum}") 

#     elif  "country" in keys:
#         print(f"hello from {kwargs[country]},the answer is {sum}")
   

#     elif not kwargs:
#         print("hello annonymous the answer is {sum}")   


# sum_and_greet(1,2,3, name="Queenter")

# sum_and_greet(10,20,30, name="Queenter",country="Kenya")  

# sum_and_greet("KImbery")  

# sum_and_greet(100,2000,3000,)       










