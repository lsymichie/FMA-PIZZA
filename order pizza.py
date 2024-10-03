# Simple Ordering Program 
print ("====================Welcome To Pizza Hut Deliveries===================")


# Input Pizza Topping
print("-----------------------------------------------")
print("\t\tPizza Topping")
print("1. Frankfurter\t\t\t| Rp 70.000")
print("2. Meat Monsa \t\t\t| Rp 85.000")
print("3. Super Supreme \t\t| Rp 45.000")
print("4. Super Supreme Chicken\t| Rp 50.000 ")

frankfurter = 70000 
meatmonsa = 85000 
super_supreme = 45000 
supersupreme_chicken = 50000 

while True:
    pizza_topping = input("Choose Pizza Topping : ")

    if pizza_topping == "1":
        topping_price = frankfurter
        break
    elif pizza_topping == "2":
        topping_price = meatmonsa
        break
    elif pizza_topping == "3":
        topping_price = super_supreme
        break
    elif pizza_topping == "4":
        topping_price = supersupreme_chicken
        break
    else:
        print("Pizza Topping Not Valid!!!")
        print("Please input a valid number")
    
# Input Pizza Crust
print("-----------------------------------------------")
print("\t\tPizza Crust")
print("1. Panpizza\t\t\t| Rp 10.000")
print("2. Stuffed Crust Sosis\t\t| Rp 15.500")
print("3. Crowncrust\t\t\t| Rp 19.000")
print("4. Cheesybites\t\t\t| Rp 22.000")

panpizza = 10000 
stuffed_crust_sosis = 15500 
crowncrust = 19000 
cheesybites = 22000 

while True:
    pizza_crust = input("Choose Pizza Crust : ")

    if pizza_crust == "1" :
        crust_price = panpizza
        break
    elif pizza_crust == "2" :
        crust_price = stuffed_crust_sosis
        break
    elif pizza_crust == "3" :
        crust_price = crowncrust
        break
    elif pizza_crust == "4" :
        crust_price = cheesybites
        break
    else:
        print("Crust Pizza not valid")
        print("Please input a valid number")

# Input Pizza Size
print("-----------------------------------------------")
print("\t\tPizza Size")
print("1. Small\t\t\t| Rp 5.000")
print("2. Medium\t\t\t| Rp 15.000")
print("3. Large\t\t\t| Rp 20.0000")

small = 5000        
medium = 15000   
large = 20000

while True:
    pizza_size = input("Choose Pizza Size : ")

    if pizza_size == "1":
        size_price = small
        break
    elif pizza_size == "2":
        size_price = medium
        break
    elif pizza_size == "3":
        size_price = large
        break
    else:
        print("Pizza Size Not Valid!!!")
        print("Please input a valid number")

print("-----------------------------------------------")
#Input Add Cheese
print("Add Cheese\t\t\t| Rp 13.000")

add_cheese = input("Do You Want To Add Cheese? (Yes/No): ")


if add_cheese == "yes":
    cheese_price = 13000  # Price of cheese Rp. 13.000
else:
    cheese_price = 0

# Calculate total price
total_price = topping_price + crust_price + size_price + cheese_price
print("-----------------------------------------------")

# Display the total price to pay
print("Thank you for choosing Pizza Hut Deliveries!")
print(f"Your final bill is: Rp.{total_price}")

print("===============================================")



