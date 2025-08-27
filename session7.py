# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
    
#     def __str__(self):
#         return f"username = {self.username} password = {self.password}"

# user1 = User("amir","amir123")
# user2 = User("amir","amir123")

# # print(type(user1))
# # print(user1.username)
# # print(user1.password)
# print(user1)


# class RectAngle:
#     def __init__(self,tol,arz):
#         self.tol= tol
#         self.arz = arz

#     def Area(self):
#         return self.tol * self.arz
    
#     def Env(self):
#         return (self.arz+self.tol)*2
    

# rect = RectAngle(10,8)
# # print(rect.tol*rect.arz)
# print(rect.Area())
# print(rect.Env())

# rect2 = RectAngle(15,10)
# print(rect2.Area())
# print(rect2.Env())

class Customer:
    def __init__(self,name,age,balance,job):
        self.name = name
        self.age = age
        self.balance = balance
        self.job = job
        self.hasLoan = False
    
    def __str__(self):
        return f"customer info: {self.name} - {self.balance} - {self.job}"

    def changeName(self,newName):
        self.name = newName
    
    def increaseBalance(self,increaseValue):
        self.balance += increaseValue

    def isValidLoan(self,loanValue):
        if self.balance >= loanValue and self.isValidLoan==False:
            return True
        else:
            return False
    
    def payLoan(self,loanValue):
        self.balance += loanValue
        self.hasLoan=True
    

customer = Customer("amir",24,1000,"teacher")

# function for handle update customer name
def updateCustomerName():
    name = input("please enter name for update: ")
    customer.changeName(name)
    print("-------------cutomer name updated---------------")

# function for hande increase customer balance
def increaseCustomerBalance():
    increaseValue = int(input("please enter increaes value: "))
    customer.increaseBalance(increaseValue)
    print("-------------balance incrased---------------")
 
# function for handle customer loan request
def loadRequest():
    loanValue = int(input("please enter loan request value: "))
    if customer.isValidLoan(loanValue):
        customer.payLoan(loanValue)
        print("-------------your loan is paid--------------")
    else:
        print("-------------you cant take loan--------------")

while True:
    option = int(input("""
1-show customer infos
2-update name
3-incraese balance
4-request Loan
5-exit
please enter option:  """))
    if option==1:
        print(customer)
    elif option==2:
        updateCustomerName()
    elif option==3:
        increaseCustomerBalance()
    elif option==4:
        loadRequest()
    elif option==5:
        break

        
