# 1. Create a list named products containing at least 6 product names
products = ["Pencil", "Pen", "Book", "Notebook", "Eraser", "Sharpener"]

# 2. Create a tuple named sample_product that stores (product_name, price, category)
sample_product = ("Pen", 25.00, "Stationery")

# 3. Print the 2nd and last product from the products list
print("2nd product:", products[1])
print("Last product:", products[-1])

# 4. Append two new product names to products and then print the updated list
products.append("Ruler")
products.append("Highlighter")
print("Updated products list:", products)

# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple
product_temp_list = list(sample_product)
product_temp_list[1] = 30.00  # changing price from 25.00 to 30.00
sample_product = tuple(product_temp_list)

print("Modified sample_product tuple:", sample_product)