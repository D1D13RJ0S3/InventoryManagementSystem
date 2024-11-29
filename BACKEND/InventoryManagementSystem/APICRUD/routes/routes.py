from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.models import Product
from config.db import get_session, create_db_and_tables

# Crear tablas al inicio
create_db_and_tables()

# Crear router
router = APIRouter()

# Endpoint GET
@router.get("/search/{id}", response_model=Product)
def search_id (id: int, session: Session = Depends(get_session)):
    statement = select(Product).where(Product.id == id)
    var_product = session.exec(statement).first()
    if not var_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return var_product

# Endpoint POST
@router.post("/add", response_model=Product)
def add_product(*, session: Session = Depends(get_session), product: Product):
    new_product = Product(**product.model_dump())  
    # se crea una variable que es un objeto Producto
    # despues se despempaqueta el argumento product para que pueda ser leido por el objeto y usar sus valores como atributos del objeto
    # despues se vuelve a transformar en un disccionario python
    session.add(new_product)
    session.commit()
    session.refresh(new_product)  # Actualiza el objeto con los datos generados (como `id`)
    return new_product

@router.get("/products", response_model=list[Product])
def get_all_products(session: Session = Depends(get_session)): # depens sirve para poner funciones
    statement = select(Product)  # Seleccionar todos los productos
    products = session.exec(statement).all()  # Ejecutar la consulta y obtener todos
    return products
