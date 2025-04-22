from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/clearancetyp", tags=["CLEARANCETYP"])

@router.get("/", response_model=list[schemas.CLEARANCETYPBase])
def get_all_clearancetyp(name: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.CLEARANCETYP)
    if name:
        query = query.filter(models.CLEARANCETYP.NAME.ilike(f"%{name}%"))
    return query.all()

@router.post("/")
def create_clearancetyp(clearance: schemas.CLEARANCETYPBase, db: Session = Depends(database.get_db)):
    db_clearance = models.CLEARANCETYP(**clearance.dict())
    db.add(db_clearance)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Created successfully"}

@router.put("/{nb}")
def update_clearancetyp(nb: int, clearance: schemas.CLEARANCETYPBase, db: Session = Depends(database.get_db)):
    db_clearance = db.query(models.CLEARANCETYP).filter(models.CLEARANCETYP.NB == nb).first()
    if not db_clearance:
        raise HTTPException(404, "Record not found")
    for key, value in clearance.dict().items():
        setattr(db_clearance, key, value)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Updated successfully"}

@router.delete("/{nb}")
def delete_clearancetyp(nb: int, db: Session = Depends(database.get_db)):
    db_clearance = db.query(models.CLEARANCETYP).filter(models.CLEARANCETYP.NB == nb).first()
    if not db_clearance:
        raise HTTPException(404, "Record not found")
    db.delete(db_clearance)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))
    return {"message": "Deleted successfully"}