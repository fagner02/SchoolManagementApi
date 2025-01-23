from sqlalchemy.orm import Session
from typing import Type, Dict, Any
from sqlmodel import SQLModel
import logging

def aplicar_filtros(
    modelo: Type[SQLModel],
    db: Session,
    filtros: Dict[str, Any]
):
  
    query = db.query(modelo)
    for campo, valor in filtros.items():
        # Verifica se o campo existe no modelo
        if hasattr(modelo, campo):
            # Se o valor for uma string, usa ilike para busca parcial
            if isinstance(valor, str):
                query = query.filter(getattr(modelo, campo).ilike(f"%{valor}%"))
            else:
                query = query.filter(getattr(modelo, campo) == valor)
    return query.all()

logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato do log
)

logger = logging.getLogger()

def log_event(message):
    logger.info(message)