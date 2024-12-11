from typing import Optional
from sqlmodel import Field, SQLModel

class ProductBase(SQLModel):
    """
    Base model for product data.

    This model defines the core attributes for a product:
    - name: The name of the product.
    - cantidad: The quantity of the product.
    - precio: The price of the product.
    """

    name: str
    cantidad: int
    precio: float

class Product(ProductBase, table=True):
    """
    Database model for a product.

    This model extends `ProductBase` and adds a unique identifier (`id`).
    It represents the database table for storing product information.

    Attributes:
        id (Optional[int]): The primary key of the product in the database.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    
class ProductCreate(ProductBase):
    """
    Model for creating a new product.

    Inherits from `ProductBase` and is used to validate input data
    when creating a new product. No additional attributes are defined.
    """
    pass

class ProductUpdate(SQLModel):
    """
    Model for updating product data.

    This model allows partial updates to product information. All fields
    are optional to facilitate updates without requiring all data.

    Attributes:
        id (Optional[int]): The unique identifier of the product.
        name (Optional[str]): The updated name of the product.
        cantidad (Optional[int]): The updated quantity of the product.
        precio (Optional[float]): The updated price of the product.
    """

    id: Optional[int] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
