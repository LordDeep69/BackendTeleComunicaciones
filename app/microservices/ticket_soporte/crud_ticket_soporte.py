from sqlalchemy.orm import Session
from .model_ticket_soporte import TicketSoporte
from .schema_ticket_soporte import TicketSoporteCreate, TicketSoporteUpdate

def get_ticket_soporte(db: Session, ticket_id: int):
    return db.query(TicketSoporte).filter(TicketSoporte.id == ticket_id).first()

def get_tickets_soporte(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TicketSoporte).offset(skip).limit(limit).all()

def create_ticket_soporte(db: Session, ticket: TicketSoporteCreate):
    db_ticket = TicketSoporte(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def update_ticket_soporte(db: Session, ticket_id: int, ticket: TicketSoporteUpdate):
    db_ticket = db.query(TicketSoporte).filter(TicketSoporte.id == ticket_id).first()
    if db_ticket:
        update_data = ticket.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_ticket, key, value)
        db.commit()
        db.refresh(db_ticket)
    return db_ticket

def delete_ticket_soporte(db: Session, ticket_id: int):
    db_ticket = db.query(TicketSoporte).filter(TicketSoporte.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket
