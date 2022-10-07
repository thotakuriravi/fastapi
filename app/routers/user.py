

from fastapi import FastAPI, APIRouter, Depends, status, HTTPException, Response
from fastapi.params import Body
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, utills


router = APIRouter(prefix="/user", tags=["Users API"])


@router.post("/", response_model=schemas.UserOut)
def UserCreation(user: schemas.User , db:Session = Depends(get_db)):

    # Hashing the Password
    hash_password = utills.hash(user.password)
    user.password = hash_password

    user_update = models.User(**user.dict())
    db.add(user_update)
    db.commit()
    db.refresh(user_update)

    return user_update


@router.get('/{id}',  response_model=schemas.UserOut)
def get_user(id:int, db:Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'User not found with the id: {id} was not found')
    
    return user

