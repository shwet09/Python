#shopping carts

foods = []
prices = []
total= 0 

while True:
    food = input("Enter a foods to buy (q to quit): ")
    if food.lower() == "q":
        break 
    else:
        price = int(input("Enter the price of {foods}: $ "))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART----")
for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total price is: ${total}")
