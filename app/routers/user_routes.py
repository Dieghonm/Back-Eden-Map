from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user_schemas import UserCreate, UserResponse
from app.controllers.user_controller import (
    create_user_controller,
    get_user_controller,
    list_users_controller
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_controller(user, db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    return get_user_controller(user_id, db)


@router.get("/", response_model=list[UserResponse])
def list_users_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return list_users_controller(skip, limit, db)
