from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Banco de dados
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Rate Limiting (requisições por hora)
    RATE_LIMIT_REGISTER: int = 2
    RATE_LIMIT_REFRESH: int = 4
    RATE_LIMIT_LOGIN: int = 6

    class Config:
        env_file = ".env"

settings = Settings()