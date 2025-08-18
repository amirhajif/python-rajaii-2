# return

# def sayHello():
#     print("hello")
# sayHello()

# name = "amir"
# print(len(name))

# length = len(name)
# print(length) 

# def multiplyTwo(n):
#     return n*2

# result = multiplyTwo(10)
# print(result)

# print(multiplyTwo(20))

def introduce(name,age,city):
    return f"my name is {name} {age} {city}"

# print(introduce("amir",24,"babol"))

def factoriel(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact


# print(factoriel(5))

def isEven(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False
    return n%2==0

# recursive funciton - توابع بازگشتی 
def sumNumbers(n):
    if n==0:
        return 0
    else:
        return n+sumNumbers(n-1)
'''
5
15
5+10
4+6
3+3
2+1
1
'''    
def recursiveFactoriel(n):
    if n==1:
        return 1
    else:
        return n*recursiveFactoriel(n-1)
    

def coffeFood(*foods):
    # print(foods)
    for food in foods:
        print(food)

def restaurantFood(**foods):
    print(foods)

# coffeFood("burger","pizza","sandwich")

# restaurantFood(burger = 100,sandwich = 200 ,pizza = 200 )

def multiplyTwo(n):
    return n*2

# lambda
m2 = lambda n:n*2
# print(m2(10))

rectangleArea = lambda tol,arz:tol*arz
# print(rectangleArea(10,8))

numbers = [1,2,3,4,5,6,7,8,9]

def multiplyFive(number):
    return number*5

# newNumbers = list(map(multiplyFive,numbers))

# newNumbers = list(map(lambda number:number*5,numbers))
# print(newNumbers)


# filteredList = list(filter(lambda number:number%2==0,numbers))
# print(filteredList)

# import functions

# functions.sayHello()
# functions.sayGoodBye()


# from functions import sayGoodBye
# sayGoodBye()

# from functions import sayName as sn
# sn()

# from functions import sayName,sayGoodBye

# from functions import *

# import math

# print(math.factorial(5))

# import time

# print(time.time())
# print("welcome ........")
# time.sleep(2)
# print("everythings is ready ......")

# import random

# print(random.randint(10,100))

# users = ["amir","reza","mohammad","jafar"]
# print(random.choice(users))

# import datetime

# now = datetime.datetime.now()
# print(now)

# print(now.strftime("%Y"))

import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
