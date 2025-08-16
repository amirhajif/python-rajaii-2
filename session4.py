'''
Collection
1-list []
2-tuple ()
3-dictionary {}
4-Set {}
'''

# cars = {"bmw","206","benz","prado","206"}
# print(cars)
# print(type(cars))

# for car in cars:
#     print(car)

# print(cars[1])

# cars.add("bugati")
# print(cars)

# remove - discard

# cars.remove("405")
# print(cars)

# cars.discard("405")
# print(cars)


myCars = {"bmw","206","benz"}
showRoomCars = {"prado","benz","haima"}

# allCars = myCars.union(showRoomCars)
# # print(allCars)

# myCars.update(showRoomCars)
# print(myCars)

# intersectionCars = myCars.intersection(showRoomCars)
# print(intersectionCars)

# myCars.intersection_update(showRoomCars)
# print(myCars)

# symmetricDifference = myCars.symmetric_difference(showRoomCars)
# print(symmetricDifference)

# userInfo = {
#     "username":"amir",
#     "password":"amir123",
#     "age":24
# }

# print(list(userInfo.values()))


numbers = [1,2,3,4,5,6]
# newNumbers = []
# for number in numbers:
#     newNumbers.append(number**2)
# print(newNumbers)

# newNumbers = [number**2 for number in numbers]

# enumerate
# users = ["amir","reza","mamad"]
# # print(list(enumerate(users)))

# for index,user in enumerate(users,start=1):
#     print(f"{index} ---> {user}")


# print("hello")


# definition
def sayHello():
    print("hello")

# call
# sayHello()

# f(x) = 3x+5
def f(x):
    print(3*x+5)


# n= int(input("please enter x: "))
# f(n)

# f(10)

# f(int(input("please enter number: ")))


# area rectangle
def rectangleArea(tol,arz):
    print(tol*arz)

# rectangleArea(10,8)

def checkEven(n):
    if n%2==0:
        print("even")
    else:
        print("odd")


# checkEven(21)

# factoriel 
def factoriel(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

# factoriel(5)

def introduce(name,city="babol",age=24):
    print(f"my name is {name} and {age} year`s old and form {city}")

# introduce(city="babol",name = "amir",age = 24)
introduce("amir","babol")
