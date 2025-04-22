from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/jabicenter", tags=["JABICENTER"])

@router.get("/", response_model=list[schemas.JABICENTERBase])
def get_all_jabicenter(name: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.JABICENTER)
    if name:
        query = query.filter(models.JABICENTER.NAME.ilike(f"%{name}%"))
    return query.all()

@router.post("/")
def create_jabicenter(jabi: schemas.JABICENTERBase, db: Session = Depends(database.get_db)):
    db_jabi = models.JABICENTER(**jabi.dict())
    db.add(db_jabi)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Created successfully"}

@router.put("/{nb}")
def update_jabicenter(nb: int, jabi: schemas.JABICENTERBase, db: Session = Depends(database.get_db)):
    db_jabi = db.query(models.JABICENTER).filter(models.JABICENTER.NB == nb).first()
    if not db_jabi:
        raise HTTPException(404, "Record not found")
    for key, value in jabi.dict().items():
        setattr(db_jabi, key, value)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Updated successfully"}

@router.delete("/{nb}")
def delete_jabicenter(nb: int, db: Session = Depends(database.get_db)):
    db_jabi = db.query(models.JABICENTER).filter(models.JABICENTER.NB == nb).first()
    if not db_jabi:
        raise HTTPException(404, "Record not found")
    db.delete(db_jabi)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Deleted successfully"}