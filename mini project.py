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
def buy_item():
    name=input("Enter the name of the item: ")
    count=int(input("Enter the count of the item: "))
    if name in inventory:
        if inventory[name]["count"]>=count:
            inventory[name]["count"]-=count
            print("Yahooo! You have purchased this item successfully")
        else:
            print("item not available")
    def change_price():
     name=input("Enter the name of the item:")
     price=int(input("Enter the new price of the item:"))
     for key , values in inventory.items():
          if key==name:
               inventory[key]["price"]=price
               print("Price updated successfully")
               break
          else:
               print("Item not available")
               exit()
               def update_inventory():
     name=input("Enter the name of the item:")
     count=int(input("Enter the new count of the item:"))
     for key , values in inventory.items():
          if key==name:
               inventory[key]["count"]=count
               print("Count updated successfully")
               break
          else:
               print("item not available")
               exit()
               def display_inventory():
     total_sale=0
     print("Inventory:")
     for key , values in inventory.items():
          print(f"{key} : {values['count']}")
          total_sale+=values['price']*values['count']
          print(f"Total sales: {total_sale}")
     