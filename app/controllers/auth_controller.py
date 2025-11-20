from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth_schemas import LoginRequest
from app.services.auth_service import login_service


def login_controller(credentials: LoginRequest, db: Session):
    """
    Controller para autenticação de usuário
    
    Args:
        credentials: Objeto com login e password
        db: Sessão do banco de dados
    
    Returns:
        dict com token e dados do usuário
        
    Raises:
        HTTPException: Se credenciais inválidas
    """
    result = login_service(
        login=credentials.login,
        password=credentials.password,
        db=db
    )
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return result