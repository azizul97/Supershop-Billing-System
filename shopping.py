foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}: $"))
        prices.append(price)
        
print("-----Your Cart-----")

for x in foods:
    print(x, end=" ")
for y in prices:
    total = total + y
    
print(f"\nYour total price is: ${total}")    
   
        