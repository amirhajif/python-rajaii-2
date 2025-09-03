# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
    
#     def __str__(self):
#         return f"{self.username} {self.password}"
    
#     def setUsername(self,newUsername):
#         self.username = newUsername
#     def getUsername(self):
#         return self.username
    
#     def setPassword(self,newPassword):
#         self.password = newPassword
#     def getPassword(self):
#         return self.password
    
# users = []

# def signup(username,password):
#     # check username not exist
#     for user in users:
#         if username == user.getUsername():
#             print("\n---------this username exist already----------\n")
#             break
#     else:
#         user = User(username,password)
#         users.append(user)
#         print("\n---------Account Created-------\n")

# def login(username,password):
#     # login ---> 1-update username 2- update password
#     for user in users:
#         if username==user.getUsername() and password == user.getPassword():
#             updateOption = int(input("1-update username\n2-update password\nenter option: "))
#             if updateOption==1:
#                 newUsername = input("please enter new username: ")
#                 user.setUsername(newUsername)
#                 print("\n--------username updated---------\n")
#             else:
#                 newPassword = input("please enter new password: ")
#                 user.setPassword(newPassword)
#                 print("\n--------password updated---------\n")
#             break
#     else:
#         print("\n----------user not exist-----------\n")

# while True:
#     option = int(input("""
# 1-signup
# 2-login
# 3-exit
# enter option: 
# """))
#     if option==1:
#         username = input("please enter username: ")
#         password = input("please enter password: ")
#         signup(username,password)
#     elif option==2:
#         username = input("please enter username: ")
#         password = input("please enter password: ")
#         login(username,password)
#     else:
#         break


# inheritance
# parent
class Person:
    def __init__(self,name,age,country,gender):
        self.name = name
        self.age = age
        self.country = country
        self.gender = gender
    
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
    
    def setCountry(self,country):
        self.country=country
    def getCountry(self):
        return self.country
    
    def setGender(self,gender):
        self.gender=gender
    def getGender(self):
        return self.gender
    
    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"
    
# child
class Employee(Person):
    def __init__(self,name,age,country,gender,salary):
        super().__init__(name,age,country,gender)
        self.salary = salary

    def setSalary(self,salary):
        self.salary=salary
    def getSalary(self):
        return self.salary
    
    def __str__(self):
        return super().__str__() + f" {self.salary}"
    

# overriding

employee = Employee("amir",24,"iran","male",1000)

print(employee)
