from fastapi import APIRouter, Depends
from typing import List
from blog import database, schemas
from sqlalchemy.orm import Session
from blog.repository import user


router = APIRouter(tags=["users"], prefix="/user")
session = Depends(database.get_db)


@router.get("", response_model=List[schemas.UserOut])
def showUsers(db: Session = session):
    return user.index(db)


@router.post("", response_model=schemas.UserOut)
def createUser(request: schemas.UserIn, db: Session = session):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.UserOut)
def getUser(id: int, db: Session = session):
    return user.show(id, db)
