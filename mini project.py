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
          def main():
    while True:
        print("1. Add an item to the inventory.")
        print("2. Buy an item from the inventory.")
        print("3. Change the price of an existing item in the inventory.")
        print("4. Update the inventory of an existing item in the inventory.")
        print("5. Display the inventory.")
        print("6. Exit the program.")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item()
           
            continue
        elif choice == 2:
            buy_item()
            
            continue
        elif choice == 3:
            change_price()
            
            continue
        elif choice == 4:
            update_inventory()
            continue
        elif choice == 5:
            display_inventory()
            
            continue
        else:
             if choice == 6:
                 
                 continue
print("Welcome to the GUN's inventory management system :")
print(inventory)       
main()
     