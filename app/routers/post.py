
from typing import List, Optional
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import get_db
from .. import models, schemas, utills, oauth2

router = APIRouter(prefix="/posts", tags=["POSTs API"])


@router.get('/', response_model=List[schemas.PostOut_Vote])
def posts(db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), limit:int = 10, offset:int = 0, search:Optional[str]=""):

    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(offset).all()
    posts = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
                    models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
                    models.Post.id).filter(models.Post.title.contains(search)).limit(
                    limit).offset(offset).all()

    return posts

@router.post("/insert",  response_model=schemas.PostOut)
def post_insert(post: schemas.Post, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    
    posts = models.Post(**post.dict(), owner_id = current_user.id)
    db.add(posts)
    db.commit()
    db.refresh(posts)

    return posts


@router.put("/update/{id}")
def post_update(id:int, post:schemas.Post, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    print(post.dict())
    post_update = db.query(models.Post).filter(models.Post.id == id)
    posts = post_update.all()

    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id : {id} was not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorized to perform requested action")
    
    post_update.update(post.dict(), synchronize_session=False)
    db.commit()
    return { "data": "Successful" }



@router.delete("/delete/{id}")
def post_delete(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_delete = db.query(models.Post).filter(models.Post.id == id)
    post = post_delete.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id : {id} was not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorized to perform requested action")

    post_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    