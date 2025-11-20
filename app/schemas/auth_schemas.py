from pydantic import BaseModel

class LoginRequest(BaseModel):
    """Schema para requisição de login"""
    login: str
    password: str

class LoginResponse(BaseModel):
    """Schema para resposta de login"""
    access_token: str
    token_type: str = "bearer"
    user: dict

    class Config:
        from_attributes = True