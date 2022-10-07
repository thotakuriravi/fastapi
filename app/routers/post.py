

from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session


from ..database import get_db
from .. import models, schemas, utills, oauth2

router = APIRouter(prefix="/posts", tags=["POSTs API"])


@router.get('/', response_model=List[schemas.PostOut])
def posts(db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    posts = db.query(models.Post).all()

    return posts


@router.post("/insert",  response_model=schemas.PostOut)
def post_insert(post: schemas.Post, db: Session = Depends(get_db)):
    
    posts = models.Post(**post.dict())
    db.add(posts)
    db.commit()
    db.refresh(posts)

    return posts



@router.put("/update/{id}")
def post_update(id:int, post:schemas.Post, db:Session = Depends(get_db)):
    print(post.dict())
    post_update = db.query(models.Post).filter(models.Post.id == id)
    posts = post_update.all()

    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id : {id} was not found')
    
    post_update.update(post.dict(), synchronize_session=False)
    db.commit()
    return { "data": "Successful" }



@router.delete("/delete/{id}")
def post_delete(id:int, db:Session = Depends(get_db)):
    post_delete = db.query(models.Post).filter(models.Post.id == id)
    post = post_delete.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id : {id} was not found')

    post_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)