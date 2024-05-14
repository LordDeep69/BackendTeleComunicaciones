from sqlalchemy.orm import Session
from .model_plan import Plan
from .schema_plan import PlanCreate, PlanUpdate

def get_plan(db: Session, plan_id: int):
    return db.query(Plan).filter(Plan.id == plan_id).first()

def get_planes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Plan).offset(skip).limit(limit).all()

def create_plan(db: Session, plan: PlanCreate):
    db_plan = Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def update_plan(db: Session, plan_id: int, plan: PlanUpdate):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if db_plan:
        update_data = plan.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_plan, key, value)
        db.commit()
        db.refresh(db_plan)
    return db_plan

def delete_plan(db: Session, plan_id: int):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if db_plan:
        db.delete(db_plan)
        db.commit()
    return db_plan
