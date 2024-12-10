from sqlmodel import Session, SQLModel, create_engine
import os

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
# Función para obtener sesiones  
def get_session():
    with Session(engine) as session:
        yield session
