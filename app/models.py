

from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base



class Post(Base):
    __tablename__ = "fposts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published =Column(Boolean, server_default = 'True', default = True)
    created_at = Column(TIMESTAMP(timezone=True), server_default = text('now()'), nullable = False)
    owner_id = Column(Integer, ForeignKey("fusers.id", ondelete="CASCADE"), nullable = False)
    owner = relationship("User")



class User(Base):
    __tablename__ = "fusers"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)


class Vote(Base):
    __tablename__ = 'fvotes'

    post_id = Column(Integer, ForeignKey("fposts.id", ondelete='CASCADE'), primary_key = True)
    user_id = Column(Integer, ForeignKey("fusers.id", ondelete='CASCADE'), primary_key = True)




