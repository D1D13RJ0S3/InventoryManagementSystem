# Run the code to understand how each method works

from classes import Product, Inventory

products_list = [
    Product(1,"banana",1500,1),
    Product(2,"onion",2000,3),
    Product(3,"tomato",500,7)
    ]
inventory = Inventory(product_list=products_list)

inventory.increase_quantity("banana",3)
inventory.decrease_quantity("tomato",2)
inventory.add_product(Product(4,"chili",800,2))
inventory.remove_product("banana")

[print(element) for element in inventory.product_list]
print(inventory.check_quantity("banana"))
print(inventory.check_quantity("tomato"))
