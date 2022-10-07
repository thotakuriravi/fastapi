


from fastapi import Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, models


oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

# Secret Key
# Algorithm
# Expire Time

SECRET_KEY = "36a3eda67bceaf1714eb070b79d66a26c6fd1432875e763bc705697a6cbdb7d1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIIRE_MINUTES = 30


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIIRE_MINUTES)
    to_encode.update( { "exp" : expire })

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")

        if not id:
            raise credentials_exception
        
        token_data = schemas.TokenData(id= id)
    except JWTError:
        raise credentials_exception
    return token_data
    
def get_current_user(token:str= Depends(oauth2_schema), db:Session = Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                            detail="Could Not found the credentials", 
                                            headers={"www-Authentication": "Bearer"} )
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user