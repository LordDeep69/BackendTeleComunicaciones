from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_ticket_soporte import (
    get_ticket_soporte, get_tickets_soporte, create_ticket_soporte,
    update_ticket_soporte, delete_ticket_soporte
)
from .schema_ticket_soporte import (
    TicketSoporteCreate, TicketSoporteUpdate, TicketSoporte
)
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tickets-soporte/", response_model=List[TicketSoporte])
def read_tickets_soporte(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tickets_soporte = get_tickets_soporte(db, skip=skip, limit=limit)
    return tickets_soporte

@router.get("/tickets-soporte/{ticket_id}", response_model=TicketSoporte)
def read_ticket_soporte(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket_soporte = get_ticket_soporte(db, ticket_id=ticket_id)
    if db_ticket_soporte is None:
        raise HTTPException(status_code=404, detail="Ticket de soporte no encontrado")
    return db_ticket_soporte

@router.post("/tickets-soporte/", response_model=TicketSoporte, status_code=status.HTTP_201_CREATED)
def create_new_ticket_soporte(ticket: TicketSoporteCreate, db: Session = Depends(get_db)):
    return create_ticket_soporte(db=db, ticket=ticket)

@router.put("/tickets-soporte/{ticket_id}", response_model=TicketSoporte)
def update_existing_ticket_soporte(ticket_id: int, ticket: TicketSoporteUpdate, db: Session = Depends(get_db)):
    db_ticket_soporte = update_ticket_soporte(db, ticket_id=ticket_id, ticket=ticket)
    if db_ticket_soporte is None:
        raise HTTPException(status_code=404, detail="Ticket de soporte no encontrado")
    return db_ticket_soporte

@router.delete("/tickets-soporte/{ticket_id}", response_model=TicketSoporte)
def delete_existing_ticket_soporte(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket_soporte = delete_ticket_soporte(db, ticket_id=ticket_id)
    if db_ticket_soporte is None:
        raise HTTPException(status_code=404, detail="Ticket de soporte no encontrado")
    return db_ticket_soporte
