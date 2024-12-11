from pydantic import BaseModel

class ProductEschema(BaseModel):
    """
    Product schema for data validation and serialization.

    This schema represents the structure of a product. It is used for 
    validating and serializing product data when interacting with the API 
    and database. The fields include product name, quantity, price, and ID.

    Attributes:
        name (str): The name of the product.
        cantidad (int): The quantity of the product in stock.
        precio (float): The price of the product.
        id (int): The unique identifier of the product.

    Example:
        ProductEschema(name="Example Product", cantidad=10, precio=19.99, id=1)
    """
    name: str
    quantity: int
    price: float
    id: int

