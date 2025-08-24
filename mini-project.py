import time
shoppingList = []

# function for add new item into list
def addItem():
    name = input("please enter item name: ")
    item = {
        "name":name,
        "done":False
    }

    shoppingList.append(item)
    print("-----------item added to list--------------\n")
    time.sleep(2)

# function for show buy items
def showItems():
    if shoppingList:
        for indx,item in enumerate(shoppingList,start=1):
            if item["done"]:
                print(f"{indx} - {item['name']}  is buy")
            else:
                print(f"{indx} - {item['name']}  not buy")
    else:
        print("\n-------------you dont have shopping items---------------\n")

# function for remove item from list
def removeItem():
    showItems()
    index = int(input("please enter item number for remove: "))
    if index>0 and index<=len(shoppingList):
        del shoppingList[index-1]
        print("\n---------item deleted-----------\n")
    else:
        print("\n---------enter number out of range-----------\n")

# function for change item status
def markDone():
    showItems()
    index = int(input("please enter item number for change status: "))
    if index>0 and index<=len(shoppingList):
        shoppingList[index-1]["done"]=True
        print("\n---------item Done!-----------\n")
    else:
        print("\n---------enter number out of range-----------\n")

# function for show not buy products
def showNotBuyItems():
    if shoppingList:
        for indx,item in enumerate(shoppingList,start=1):
            if not item["done"]:
                print(f"{indx} - {item['name']}")
             
    else:
        print("\n-------------you dont have shopping items---------------\n")

while True:
    option = int(input("""
----- Shopping List -----
1. Show shopping list
2. Add new item
3. Remove item
4. Mark item as "Purchased"
5. Show only unpurchased items
6.  Exit
Your choice: """))
    if option==1:
        showItems()
    elif option==2:
        addItem()
    elif option==3:
        removeItem()
    elif option==4:
        markDone()
    elif option==5:
        showNotBuyItems()
    elif option==6:
        break
