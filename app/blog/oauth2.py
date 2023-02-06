from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from blog import JWT


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWT.verify_token(token, credentials_exception)
