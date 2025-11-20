from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth_schemas import LoginRequest, LoginResponse
from app.controllers.auth_controller import login_controller

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login_route(credentials: LoginRequest, db: Session = Depends(get_db)):
    """
    Rota de autenticação
    
    Recebe login e senha, retorna token JWT e dados do usuário
    
    Args:
        credentials: Objeto com login e password
        db: Sessão do banco de dados (injetada automaticamente)
    
    Returns:
        LoginResponse com token JWT e dados do usuário
    
    Example:
        POST /auth/login
        {
            "login": "dieghonm",
            "password": "Admin123@"
        }
        
        Response:
        {
            "access_token": "eyJhbGc...",
            "token_type": "bearer",
            "user": {
                "id": 1,
                "login": "dieghonm",
                "email": "dieghonm@gmail.com",
                "tag": "admin",
                "plan": "admin"
            }
        }
    """
    return login_controller(credentials, db)