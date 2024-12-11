from sqlmodel import Session, SQLModel, create_engine
from database.db_config import settings

# Construct the database connection URL
db_url = f"sqlite:///{settings.db_sqlite}"
engine = create_engine(db_url)
with engine.connect() as connection:
    print("conexion exitosa a la base de datos")

def create_db_and_tables():
    """
    Create the database schema and tables.

    This function initializes the database by creating all tables defined
    in the SQLModel metadata. It connects to the database engine and
    applies the schema to the database.
    """
    SQLModel.metadata.create_all(engine)
    
def get_session():
    """
    Provide a session for database operations.

    This function yields a session object that can be used to interact with
    the database. The session is automatically closed once the operation is
    complete.

    Yields:
        Session: A session object for interacting with the database.
    """
    with Session(engine) as session:
        yield session



