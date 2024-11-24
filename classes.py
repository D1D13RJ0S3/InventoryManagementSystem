#WARNING
"""
we weill not create the integration "PEPS" and the integration "UEPS",
because  that will be done in the backend integration phase

"""
class Product:
    def __init__(self, ID: int, name: str, price: int, quantity: int):
        # we received the  attributes of  ID, name, price, and quantity
        self.ID = ID 
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"ID:{self.ID}, Name:{self.name}, Price:{self.price}, Quantity:{self.quantity}"
        # this method is used for when  you want to make a "prinnt" of the object 

#we have to create a "list" of objects "Product" for send as  an attribute to the class "inventory"

class Inventory:
    def __init__(self, product_list: list):
        self.product_list = product_list
        
    def increase_quantity(self, name: str, amount_to_add: int): 
        for obj in self.product_list:
            if name == obj.name:
                obj.quantity += amount_to_add
                return obj.quantity
        return None
    
    def decrease_quantity(self, name: str, amount_to_subtract: int):
        for obj in self.product_list:
            if name == obj.name:
                if amount_to_subtract > obj.quantity:
                    print("Not enough quantity to decrease.")
                    return obj.quantity  
                else:
                    obj.quantity -= amount_to_subtract
                    return obj.quantity
        return None
    
    def add_product(self, product: object):
        for obj in self.product_list:
            if obj.name == product.name or obj.ID == product.ID:
                return self.product_list
            
        self.product_list.append(product)
        return self.product_list
                 
    def remove_product(self, name: str):
        for obj in self.product_list:
            if obj.name == name:
                self.product_list.remove(obj)
                return True 
        return False
                
    def check_quantity(self, name: str):
        for obj in self.product_list:
            if obj.name == name:
                return obj.quantity 
        return None
