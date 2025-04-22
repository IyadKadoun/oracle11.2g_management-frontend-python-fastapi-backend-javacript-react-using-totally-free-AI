from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/collector", tags=["COLLECTOR"])

@router.get("/", response_model=list[schemas.COLLECTORBase])
def get_all_collector(
    username: str = None,
    dept: str = None,
    center: str = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.COLLECTOR)
    if username:
        query = query.filter(models.COLLECTOR.USERNAME.ilike(f"%{username}%"))
    if dept:
        query = query.filter(models.COLLECTOR.DEPT == dept)
    if center:
        query = query.filter(models.COLLECTOR.CENTER == center)
    return query.all()

@router.post("/")
def create_collector(collector: schemas.COLLECTORBase, db: Session = Depends(database.get_db)):
    db_collector = models.COLLECTOR(**collector.dict())
    db.add(db_collector)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Created successfully"}

@router.put("/{username}")
def update_collector(username: str, collector: schemas.COLLECTORBase, db: Session = Depends(database.get_db)):
    db_collector = db.query(models.COLLECTOR).filter(models.COLLECTOR.USERNAME == username).first()
    if not db_collector:
        raise HTTPException(404, "Record not found")
    for key, value in collector.dict().items():
        setattr(db_collector, key, value)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Updated successfully"}

@router.delete("/{username}")
def delete_collector(username: str, db: Session = Depends(database.get_db)):
    db_collector = db.query(models.COLLECTOR).filter(models.COLLECTOR.USERNAME == username).first()
    if not db_collector:
        raise HTTPException(404, "Record not found")
    db.delete(db_collector)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Deleted successfully"}