from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schemas, database, models, JWT
from blog.hashing import Hash


router = APIRouter(tags=["authentication"], prefix="/auth")
session = Depends(database.get_db)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Password does not match the email",
        )

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWT.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
