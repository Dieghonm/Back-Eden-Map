from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user_schemas import UserCreate
from app.services.auth_service import generate_tokens_for_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user_service(user: UserCreate, db: Session, ip_address: str = None, user_agent: str = None):
    """
    Cria um novo usuário e retorna tokens de autenticação
    
    Args:
        user: Dados do usuário a ser criado
        db: Sessão do banco de dados
        ip_address: IP do cliente (opcional)
        user_agent: User agent do cliente (opcional)
    
    Returns:
        dict com access_token, refresh_token e dados do usuário
    """
    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        login=user.login,
        password=hashed_password,
        email=user.email,
        tag=user.tag or "client",
        plan=user.plan or "trial"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Gerar tokens para o novo usuário
    tokens = generate_tokens_for_user(new_user, db, ip_address, user_agent)
    
    return tokens


def get_user_service(user_id: int, db: Session):
    """Busca um usuário por ID"""
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


def list_users_service(skip: int, limit: int, db: Session):
    """Lista usuários com paginação"""
    return db.query(User).offset(skip).limit(limit).all()
