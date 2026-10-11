Snack_name = "popcorn"
Price      = 3.50
quantity = 10
is_available = True

print("snack:", (Snack_name))
print("price: $", Price)
print("In stock: ", quantity)
print("available?", is_available)

print(type(Snack_name))
print(type(Price))
print(type(quantity))
print(type(is_available))

total = Price * quantity 
print("Total value: $", total)
print("Sale Price: $", Price - 0.25)
print("Double stock:", quantity * 2)


print("Is price under $2?", Price < 2)
print("More than 5 in stock?", Price > 5)
print("Is price exactly $1.50", Price == 3.50)



shop_name = "Quick" + " " +"Bites"
print("Shop_name:", shop_name)
print("Letters in snack name:", len(Snack_name))
print("First letter:", Snack_name[0])


price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)