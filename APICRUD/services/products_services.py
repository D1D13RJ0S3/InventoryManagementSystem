from sqlmodel import Session
from models.products import Product

def get_by_id(session: Session, id: int):
    """
    Retrieve a product by its ID from the database.

    This function queries the database to retrieve a product based on 
    the provided product ID. It uses SQLAlchemy's `session.get` method 
    to fetch the product.

    Args:
        session (Session): The database session used to query the database.
        id (int): The unique identifier of the product to retrieve.

    Returns:
        Product | None: The product object if found, or None if no product 
                        with the given ID exists.

    Example:
        product = get_by_id(session, 1)
        if product:
            print(product.name)
        else:
            print("Product not found")
    """
    return session.get(Product, id)

