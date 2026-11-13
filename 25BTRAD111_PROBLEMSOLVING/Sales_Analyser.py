products = []
sales_data = {}

def add_product():
    name = input("Enter product name: ")

    if name in products:
        print("Product already exists! Use Update option.")
    else:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price per product: "))

        products.append(name)
        sales_data[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added successfully!")


def update_product():
    name = input("Enter product name to update: ")

    if name in products:
        quantity = int(input("Enter new quantity sold: "))
        price = float(input("Enter new price: "))

        sales_data[name]["quantity"] = quantity
        sales_data[name]["price"] = price

        print("Sales record updated successfully!")
    else:
        print("Product not found!")


def display_sales():
    print("\n------ PRODUCT SALES DETAILS ------")

    if not products:
        print("No sales records available.")
        return

    for name in products:
        quantity = sales_data[name]["quantity"]
        price = sales_data[name]["price"]
        revenue = quantity * price

        print("\nProduct:", name)
        print("Quantity Sold:", quantity)
        print("Price:", price)
        print("Revenue:", revenue)


def total_sales():
    total = 0

    for name in products:
        quantity = sales_data[name]["quantity"]
        price = sales_data[name]["price"]

        total = total + (quantity * price)

    print("\nTotal Sales Revenue: Rs.", total)


def highest_selling():
    if not products:
        print("No products available!")
        return

    max_quantity = -1
    highest_products = []

    for name in products:
        quantity = sales_data[name]["quantity"]

        if quantity > max_quantity:
            max_quantity = quantity
            highest_products = [name]
        elif quantity == max_quantity:
            highest_products.append(name)

    print("\nHighest Selling Product(s):")
    for name in highest_products:
        print(name, "- Quantity:", max_quantity)


# Main Menu

while True:
    print("\n===== SALES DATA ANALYZER =====")
    print("1. Add Product")
    print("2. Update Product Sales")
    print("3. Display Sales Details")
    print("4. Calculate Total Sales")
    print("5. Find Highest Selling Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        display_sales()

    elif choice == "4":
        total_sales()

    elif choice == "5":
        highest_selling()

    elif choice == "6":
        print("Thank you for using Sales Data Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")
