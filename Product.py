class Prod:
    def __init__(self, name, price, quantity, type): #constructor function
        self.name = name
        self.price = float(price[:-3]) # -3 will remove the ' RS' from the price and the price will be converted to float type
        self.quantity = int(quantity)
        self.type = type

    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.type}"
    

# List of all the products that should be fed in the input
p = [
    Prod("lettuce", "10.5 RS", 50, "Leafy green"),
    Prod("cabbage", "20 RS", 100, "Cruciferous"),
    Prod("pumpkin", "30 RS", 30, "Marrow"),
    Prod("cauliflower", "10 RS", 25, "Cruciferous"),
    Prod("zucchini", "20.5 RS", 50, "Marrow"),
    Prod("yam", "30 RS", 50, "Root"),
    Prod("spinach", "10 RS", 100, "Leafy green"),
    Prod("broccoli", "20.2 RS", 75, "Cruciferous"),
    Prod("garlic", "30 RS", 20, "Leafy green"),
    Prod("silverbeet", "10 RS", 50, "Marrow"),
]

# Output 1: Print the total number of products in the list.
print("\n\nOutput 1: Total number of products in the list:",len(p)) 

# Output 2: Add a new product (Potato,10RS, 50, Root). And print the list of all products and a total number of products(integer).

# Add potato
print("\n\nOutput 2: Adding Potato to the list of 10 RS and 50 quantity and of Root type")
name=input("Enter product name: ")
price=input("Enter price of the product: ")
quantity=int(input("Enter quantity of the product: "))
type=input("Enter type of the product: ")
new_prod = Prod(name, price, quantity, type)
#new_prod = Prod("Potato", "10 RS", 50, "Root")
p.append(new_prod)

# Print the list of all products and total number of products after adding potato
print("\nList of all the products:")
for item in p:
    print("  ",item)
print("Total number of products:",len(p))

#Output 3: Print all the products of which have the type Leafy green.
print("\n\nOutput 3: All Leafy green products:")
leafy = [item for item in p if item.type == "Leafy green"]
for leafy_prod in leafy:
    print("  ",leafy_prod)

#Output 4: As all the garlic is sold out, Remove Garlic from the list and print the total number of products that are left on the list.
print("\n\nOutput 4: Garlic is Sold out, Products available in the list are:")
for item in p:
    if item.name == "garlic":
        p.remove(item) #remove garlic from list
        break 

for item in p:
    print("  ",item) #print the list without garlic
print("Total number of products after removing Garlic:",len(p))

#Output 5: If the user adds 50 cabbages to the inventory, print the final quantity of cabbage in the inventory.
print("\n\nOutput 5: Restocking Cabbages by 50 in quantity:")
for item in p:
    if item.name == "cabbage":
        item.quantity += 50
        print('  Summary of cabbage : ', item)
        break
# Print the final quantity of cabbage in the inventory
print("Final quantity of cabbage in the inventory:",item.quantity)

#Output 6: If a user purchases 1kg lettuce, 2 kg zucchini, 1 kg broccoli the what is the round figure that the user needs to pay?
print("\n\nOutput 6: Purchasing 1kg lettuce, 2 kg zucchini, 1 kg broccoli : ")
buy_item = {"lettuce": 1, "zucchini": 2, "broccoli": 1} #storing the items in a dictionary so that we can iterate any type of item in future
total_cost=0.0
for buy_name, buy_quantity in buy_item.items():
    for item in p:
        if item.name == buy_name: #comparing the items in purchaselist with product list
            print(f'   Cost of {buy_quantity} {buy_name} is {item.price*buy_quantity}')
            total_cost += item.price * buy_quantity #adding up the cost
print("Total cost for the purchase in round figure:",round(total_cost),"RS") #rounding the total cost and printing it
