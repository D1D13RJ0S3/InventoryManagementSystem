from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.products import Product, ProductUpdate, ProductCreate
from database.database import get_session, create_db_and_tables
from schemas.products import ProductEschema
from services.products_services import get_by_id

# Initialize the database and create tables if they don't exist
create_db_and_tables()

router = APIRouter()

@router.get("/search/{id}", response_model=ProductEschema)
async def search_id(id: int, session: Session = Depends(get_session)):
    """
    Retrieve a product by its ID.

    This endpoint allows searching for a product by its unique ID. 
    If the product is found, it returns the product details, otherwise,
    it raises a 404 error with a "Product not found" message.

    Args:
        id (int): The ID of the product to search for.
        session (Session): The database session dependency.

    Raises:
        HTTPException: If the product is not found, a 404 error is raised.

    Returns:
        ProductEschema: The product details corresponding to the given ID.
    """
    var_product = get_by_id(session, id)
    if not var_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return var_product

@router.post("/add", response_model=ProductEschema)
async def add_product(*, session: Session = Depends(get_session), product: ProductCreate):
    """
    Add a new product to the database.

    This endpoint allows adding a new product by providing product details 
    in the request body. It creates a new product record and returns the 
    created product.

    Args:
        session (Session): The database session dependency.
        product (ProductCreate): The product data to create a new product.

    Returns:
        ProductEschema: The newly created product details.
    """
    new_product = Product(**product.model_dump())  
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product

@router.get("/products", response_model=list[ProductEschema])
async def get_all_products(session: Session = Depends(get_session)): 
    """
    Retrieve all products from the database.

    This endpoint retrieves a list of all products in the database and
    returns them as a list of product details.

    Args:
        session (Session): The database session dependency.

    Returns:
        list[ProductEschema]: A list of all products in the database.
    """
    statement = select(Product)
    products = session.exec(statement).all()
    return products

@router.delete("/delete/{id}")
async def delete_by_id(*, session: Session = Depends(get_session), id: int):
    """
    Delete a product by its ID.

    This endpoint allows deleting a product by its unique ID. If the product 
    exists, it is removed from the database, otherwise, a 404 error is raised.

    Args:
        session (Session): The database session dependency.
        id (int): The ID of the product to delete.

    Raises:
        HTTPException: If the product is not found, a 404 error is raised.

    Returns:
        dict: A success message indicating that the product has been deleted.
    """
    product = get_by_id(session, id)
    if not product:
        raise HTTPException(status_code=404, detail="no existe el producto solicitado")
    session.delete(product)
    session.commit()
    return {"Success"}

@router.patch("/update/{id}", response_model=ProductEschema)
async def product_update_by_id(*, session: Session = Depends(get_session), id: int, product: ProductUpdate):
    """
    Update product details by its ID.

    This endpoint allows partially updating a product's attributes by 
    providing a request body with the fields to update. If the product is
    not found, a 404 error is raised.

    Args:
        session (Session): The database session dependency.
        id (int): The ID of the product to update.
        product (ProductUpdate): The product data to update.

    Raises:
        HTTPException: If the product is not found, a 404 error is raised.

    Returns:
        ProductEschema: The updated product details.
    """
    product_obj = get_by_id(session, id)
    
    if not product_obj:
        raise HTTPException(status_code=404, detail="no existe el elemento que deseas consultar")
    
    product_data = product.model_dump(exclude_unset=True)
    for key, value in product_data.items():
        setattr(product_obj, key, value)

    session.add(product_obj)
    session.commit()
    session.refresh(product_obj)
    return product_obj
