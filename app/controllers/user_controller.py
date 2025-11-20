from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserCreate
from app.services.user_service import (
    create_user_service,
    get_user_service,
    list_users_service
)


def create_user_controller(user: UserCreate, db: Session):
    print(user)
    response = create_user_service(user, db)
    return response


def get_user_controller(user_id: int, db: Session):
    """Controller para buscar usuário"""
    return get_user_service(user_id, db)


def list_users_controller(skip: int, limit: int, db: Session):
    """Controller para listar usuários"""
    return list_users_service(skip, limit, db)
