from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user_schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user_service(user: UserCreate, db: Session):
    """Cria um novo usuário"""
    # Verificar se login já existe
    user_exists = db.query(User).filter(User.login == user.login).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login already registered"
        )
    # Verificar se email já existe
    email_exists = db.query(User).filter(User.email == user.email).first()
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    # Hash da senha
    hashed_password = pwd_context.hash(user.password)
    # Criar usuário
    new_user = User(
        login=user.login,
        password=hashed_password,
        email=user.email,
        tag=user.tag,
        plan=user.plan
    )
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


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
    """Lista todos os usuários com paginação"""
    return db.query(User).offset(skip).limit(limit).all()
