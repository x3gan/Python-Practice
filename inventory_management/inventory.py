class Item:
    def __init__ (self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

Inventory = []
till_balance = 9

def CreateItem(name, quantity, price):
    item = Item(name, quantity, price)
    return item

def AddItemToInventory(item):
    Inventory.append(item)

def FindItem(lookName):
    for element in Inventory:
        if element.name == lookName:
            print("Name: " + element.name)
            print("Quantity: " + str(element.quantity))
            print("Price: " + str(element.price))

def UpDateItem(itemUpdateName, itemUpdateQuantity, itemUpdatePrice):
    for item in Inventory:
        if item.name == itemUpdateName:
            item.quantity = itemUpdateQuantity
            item.price = itemUpdatePrice


def DeleteItem(deleteName):
    for item in Inventory:
        if item.name == deleteName:
            Inventory.remove(item)
    

def TotalStock():
    if len(Inventory) == 0:
        print("Inventory is empty")
    else:
        for element in Inventory:
            print("Name: " + element.name, ", Quantity: " + str(element.quantity), ", Price: " + str(element.price))

def PurchaseItem(itemName, itemQuantity):
    global till_balance #bc it is declared outside but python doesnt know that and thinks it is only here and says it doesnt have a starting value
    success = False

    for item in Inventory:
        if item.name == itemName:
            item.quantity -= itemQuantity
            till_balance += item.price * itemQuantity
            
            success = True
            break

    if success == False:
        print("Item not found")
    else:
        print("Purchase successful")
        print("Till balance: " + str(till_balance))
        


def ReturnItem(returnName, returnQuantity):
    global till_balance
    success = False

    for item in Inventory:
        if item.name == returnName:
            item.quantity += returnQuantity
            till_balance -= item.price * returnQuantity

            success = True
            break

    if success == False:
        print("Item not found")
    else:
        print("Return successful")
        print("Till balance: " + str(till_balance))
    

print("Create 3 items: ")
print("----------------")

item = CreateItem("apple", 10, 1)
AddItemToInventory(item)
print("Added item to inventory ")
print("------------------------")

item = CreateItem("banana", 20, 2)
AddItemToInventory(item)
print("Added item to inventory ")
print("------------------------")

item = CreateItem("orange", 30, 3)
AddItemToInventory(item)
print("Added item to inventory ")
print("------------------------")

print("Total stock: ")
print("-------------")

TotalStock()

print("Till balance: ")
print("--------------")

print(till_balance)

print("Find item data: ")
print("----------------")

FindItem("apple")

print("Delete item from inventory: ")
print("---------------------------")
DeleteItem("apple")
TotalStock()

item = CreateItem("apple", 10, 1)
AddItemToInventory(item)
print("Added item to inventory ")
print("------------------------")

print("Updated item data ")
print("-----------------")

UpDateItem("apple", 20, 2)

print("Total stock: ")
print("-------------")

TotalStock()

print("Purchase item: ")
print("--------------")

PurchaseItem("apple", 5)

print("Total stock: ")
print("-------------")

TotalStock()

print("Return item: ")
print("-------------")

ReturnItem("apple", 5)

print("Total stock: ")
print("-------------")

TotalStock()