from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    # -----------------------------------------
    # Identificação
    # -----------------------------------------
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    # -----------------------------------------
    # Credenciais
    # -----------------------------------------
    password = Column(String, nullable=False)

    # -----------------------------------------
    # Assinatura / Plano
    # -----------------------------------------
    tag = Column(String, nullable=True)
    plan = Column(String, nullable=True)
    plan_date = Column(DateTime, nullable=True)

    # -----------------------------------------
    # Senha temporária
    # -----------------------------------------
    temp_password = Column(String, nullable=True)
    temp_password_expires = Column(DateTime, nullable=True)

    # -----------------------------------------
    # Dados do usuário (emocionais / caminhos)
    # -----------------------------------------
    selected_feelings = Column(JSON, nullable=True)
    selected_path = Column(String, nullable=True)
    test_results = Column(JSON, nullable=True)

    # -----------------------------------------
    # Progresso
    # -----------------------------------------
    progress = Column(JSON, nullable=True)
    progress_updated_at = Column(DateTime, nullable=True)

    # -----------------------------------------
    # Datas de sistema
    # -----------------------------------------
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
