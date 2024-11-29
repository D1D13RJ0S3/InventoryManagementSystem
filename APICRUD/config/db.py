from sqlmodel import Session, SQLModel, create_engine

# Configuración del motor
engine = create_engine(
    'postgresql://databasedidier_user:1lPiwUxNLn5GNNAnJk5hQTsyHnU57eDa@dpg-ct3rb30gph6c73c2agpg-a.oregon-postgres.render.com/databasedidier',
    echo=True
)

# Crear tablas y datos iniciales
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Función para obtener sesiones  
def get_session():
    with Session(engine) as session:
        yield session 