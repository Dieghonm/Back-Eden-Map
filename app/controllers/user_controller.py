from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user_schemas import UserCreate
from app.services.user_service import (
    create_user_service,
    get_user_service,
    list_users_service
)
from app.services.validators import (validate_user_exists, validate_email_exists)

def create_user_controller(user: UserCreate, db: Session):
    print(user)
    email_exists = validate_email_exists(user.email, db)
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    login_exists = validate_user_exists(user.login, db)
    if login_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login already registered"
        )
    response = create_user_service(user, db)
    return response


def get_user_controller(user_id: int, db: Session):
    """Controller para buscar usuário"""
    return get_user_service(user_id, db)


def list_users_controller(skip: int, limit: int, db: Session):
    """Controller para listar usuários"""
    return list_users_service(skip, limit, db)
