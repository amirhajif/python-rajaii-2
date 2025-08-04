# seasson = int(input("please enter seasson: "))
# if seasson==1:
#     print("bahar")
# elif seasson==2:
#     print("tabestan")
# elif seasson==3:
#     print("paizz")
# elif seasson==4:
#     print("zemestan")
# else:
#     print("out of range")


# seasson = int(input("please enter seasson: "))
# match seasson:
#     case 1:
#         print("bahar")
#     case 2:
#         print("tabestan")
#     case 3:
#         print("paiiz")
#     case 4:
#         print("zemestan")
#     case _:
#         print("out of range!")
    
# users=["amir","reza","jafar"]
# username=input("please enter username: ")
# in
# if username in users:
#     print("welcome")
# else:
#     print("please signup")

# if username not in users:
#     print("please signup")
# else:
#     print("welcome")

# sentence = "salam amir khosh amadi"
# word="amir"
# if word in sentence:
#     print("exist")
# else:
#     print("not exist")

# users=["amir"]
# if len(users)==0:
#     print("empty")
# else:
#     print("not-empty")

# if users:
#     print("not-empty")
# else:
#     print("empty")

'''
Loop
1-For
2-While
'''

# names = ["amir","reza","ahmad","mohammad"]
# for name in names:
#     print(f"welcome {name}")

# scores = [10,15,5,6,9]
# sum=0
# for score in scores:
#     # sum = sum+score
#     sum+=score
# print(sum)

# numbers = [10,-1,21,124,42,-24,-6]
# positiveCounter=0
# negativeCounter=0
# for number in numbers:
#     if number>=0:
#         positiveCounter+=1
#     else:
#         negativeCounter+=1
# print(positiveCounter , negativeCounter)

# print(list(range(0,10)))
# 10 bar print("hello")

# for i in range(0,10):
#     print("hello")

# darayft adad va namayesh az 1 ta on adad
'''
10
1
2
3
...
10
'''

# number= int(input("please enter number: "))
# for i in range(1,number+1):
#     print(i)

'''
range(1,number+1) ---> [1,2,3,4,5,6,7,8]
for i in range..---->
'''

# for i in range(0,10):
#     print("hello")

# break,continue
# for i in range(0,10):
#     if i == 6 :
#         break
#     else:
#         print(i)

# print("out of loop")


# for i in range(0,10):
#     if i == 6 :
#         continue
#     else:
#         print(i)
        
# print("out of loop")


# number = int(input("please enter number: "))
# maghsom alieh haye number ra namayesh dahid
'''
6-->1,2,3,6
'''
# for i in range(1,number+1):
#     # [1,2,3,4,5,6]
#     if number%i==0:
#         print(i)

# factoriel --> 5 =1*2*3*4*5 =120
number = int(input("please enter number: "))
fact=1
for i in range(1,number+1):
    fact*=i
print(fact)
