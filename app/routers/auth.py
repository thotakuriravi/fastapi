
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, schemas, utills, oauth2, database

router = APIRouter(tags = ['Authentication'])

@router.post('/login', response_model=schemas.TokenOut)
def login(user_credentials: OAuth2PasswordRequestForm =Depends() ,db:Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    HTTP_Invalid_Credentials = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not user :
        raise HTTP_Invalid_Credentials

    if not utills.verify_password(user_credentials.password, user.password):
        raise HTTP_Invalid_Credentials

    # Token creation 
    access_token = oauth2.create_access_token(data={"user_id":user.id})

    return { "access_token": access_token, "token_type": "Bearer"}

