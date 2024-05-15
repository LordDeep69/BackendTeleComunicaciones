from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_plan import get_plan, get_planes, create_plan, update_plan, delete_plan
from .schema_plan import PlanCreate, PlanUpdate, Plan
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/planes/", response_model=List[Plan])
def read_planes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    planes = get_planes(db, skip=skip, limit=limit)
    return planes

@router.get("/planes/{plan_id}", response_model=Plan)
def read_plan(plan_id: int, db: Session = Depends(get_db)):
    db_plan = get_plan(db, plan_id=plan_id)
    if db_plan is None:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return db_plan

@router.post("/planes/", response_model=Plan, status_code=status.HTTP_201_CREATED)
def create_new_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    return create_plan(db=db, plan=plan)

@router.put("/planes/{plan_id}", response_model=Plan)
def update_existing_plan(plan_id: int, plan: PlanUpdate, db: Session = Depends(get_db)):
    db_plan = update_plan(db, plan_id=plan_id, plan=plan)
    if db_plan is None:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return db_plan

@router.delete("/planes/{plan_id}", response_model=Plan)
def delete_existing_plan(plan_id: int, db: Session = Depends(get_db)):
    db_plan = delete_plan(db, plan_id=plan_id)
    if db_plan is None:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return db_plan
