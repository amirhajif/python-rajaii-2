# allowed_names=["amir","ali","ahmad","reza"]

# has_card = input("do you have card?(yes/no) ").lower()
# name = input("please enter name: ")
# password = input("please enter password: ")

# # if has_card=="yes" and name in allowed_names and (password=="guest" or password=="temp"):
# #     print("welcome")
# # else:
# #     print("cant come")

# is_card_ok = has_card=="yes"
# is_name_ok = name in allowed_names
# is_password_ok = password in ["guest","temp"]

# if is_card_ok and is_name_ok  and is_password_ok:
#     print("welcome")
# else:
#     print("cant come")

# is_ok = True
# # if is_ok==True:
# #     print("ok")
# # else:
# #     print("not-ok")
# if is_ok:
#     print("ok")
# else:
#     print("not-ok")


# for i in range(0,5):
#     print("hello")

# i=0
# while i<5:
#     print("hello")
#     i+=1


# factoriel
# 5 --> 1*2*3*4*5
# number = int(input("please enter number: "))
# i,fact=1,1
# while i<=number:
#     fact*=i
#     i+=1
# print(fact)


# 246 = 12
'''
sum=0
246%10 = 6 --> sum+6=6 -->24
24%10 = 4 --> sum+4 = 6+4 =10 ---> 2
2%10 = 2 ---> sum+2 = 10+2 = 12 -->0
'''


# n=int(input("please enter number: "))
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# print(sum)

# get students score untill enter -1

# sum=0
# count=0
# while True:
#     score = int(input("please enter score: "))
#     if score==-1:
#         break
#     sum+=score
#     count+=1

# print(sum/count)
    
'''
1-say hello
2-say goodby
3-say name
4-exit
'''

# while True:
#     option = int(input("1-hello\n2-goodbye\n3-name\n4-exit\nenter option: "))
#     if option==1:
#         print("hello")
#     elif option==2:
#         print("bye")
#     elif option==3:
#         print("amir")
#     else:
#         break


'''
Collection = +1-list[] 2-tuple() +3- dictionary 4-set
'''

# Tuple
# salaries = (1000,15000,18000)
# # # salaries[1]=1000

# # for salary in salaries:
# #     print(salary)



# # dictionary
# student = {
#     "name":"amirhossein",
#     "schoolName":"sani",
#     "average":2
# }

# # print(student)
# # print(type(student))
# # print(student["schoolName"])

# student["average"]=20
# print(student)

# student["lastName"]="hajitabar"
# print(student)

# # print(student["fatherName"])
# print(student.get("fatherName","this key not exist"))

# del student["schoolName"]
# print(student)


# user = {
#     "username":"amir",
#     "pasword":"amir123",
#     "role":"admin"
# }

'''
username ---> amir
password ---> 
.....
'''

# print(user.items())

# for key,value in user.items():
#     print(f"{key} ----- > {value}")

# print(user.keys())
# print(user.values())

# for key in user.keys():
#     print(key)

# for value in user.values():
#     print(value)


users = {
    "amir":"123",
    "reza":"r123",
    "mamad":"m546"
}

username = input("please enter username: ")
# if username in users.keys():
#     print("already exist")
# else:
#     print("welcome")

if username in users:
        print("already exist")
else:
    print("welcome")
