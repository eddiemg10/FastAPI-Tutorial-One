from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import Hash


def index(db: Session):
    users = db.query(models.User).all()
    return users


def create(request: schemas.UserIn, db: Session):
    hashed_passwd = Hash.encrypt(request.password)
    user = models.User(name=request.name, password=hashed_passwd, email=request.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} does not exist",
        )
    return user
