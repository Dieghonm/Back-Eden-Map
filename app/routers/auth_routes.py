# app/routers/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt

from app.core.database import get_db
from app.core.config import settings


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(login: str, password: str, db: Session = Depends(get_db)):
    """
    Rota de login
    
    Args:
        login: Login do usuário
        password: Senha do usuário
    
    Returns:
        Token JWT e dados do usuário
    """
    # Buscar usuário pelo login
    # user = db.query(User).filter(User.login == login).first()
    print('user')
    
    return {
        "access_token": 'access_token',
        "user": {
            "id": 'user.id',
            "login": 'user.login',
            "email": 'user.email',
            "tag": 'user.tag',
            "plan": 'user.plan'
        }
    }