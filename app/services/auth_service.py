from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha está correta"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Cria um token JWT"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def authenticate_user(login: str, password: str, db: Session):
    """
    Autentica o usuário verificando login e senha
    
    Returns:
        User object se autenticado, None caso contrário
    """
    # Buscar usuário pelo login
    user = db.query(User).filter(User.login == login).first()
    
    if not user:
        return None
    
    # Verificar senha
    if not verify_password(password, user.password):
        return None
    
    return user


def login_service(login: str, password: str, db: Session):
    """
    Serviço de login que retorna token e dados do usuário
    
    Returns:
        dict com access_token e informações do usuário
    """
    # Autenticar usuário
    user = authenticate_user(login, password, db)
    
    if not user:
        return None
    
    # Criar token JWT
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "login": user.login,
            "tag": user.tag
        }
    )
    
    # Montar resposta
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "login": user.login,
            "email": user.email,
            "tag": user.tag,
            "plan": user.plan
        }
    }