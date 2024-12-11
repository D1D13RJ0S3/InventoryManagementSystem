from pydantic_settings import BaseSettings

sqlite_file_name = "DatabaseDefault.db"

class Settings(BaseSettings):
    db_sqlite: str = sqlite_file_name
    
settings = Settings()