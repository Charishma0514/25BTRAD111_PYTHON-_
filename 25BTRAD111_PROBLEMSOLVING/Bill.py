print("===== BILL GENERATOR =====")

name = input("Enter customer name: ")

item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n===== BILL =====")
print("Customer Name:", name)
print("Item:", item)
print("Price: ₹", price)
print("Quantity:", quantity)
print("Total: ₹", total)
print("================")
print("Thank you!")
