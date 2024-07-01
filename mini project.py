inventory={
    "9mm Pistol": {"price":20, "count":100},
    "Ak-47": {"price":30, "count":50},
    "Shotgun": {"price":10, "count":200},
    "Uzi": {"price":10, "count":200},
    }
def add_item():
   name=input("Enter the name of the item: ")
   price=int(input("Enter the price of the item: "))
   count=int(input("Enter the count of the item: "))
   inventory[name]={"price":price, "count":count}
   return print(inventory)
    