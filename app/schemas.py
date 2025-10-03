from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_verified_author: bool = False
    avatar: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    registered_at: datetime

    class Config:
        from_attributes = True

class NewsBase(BaseModel):
    title: str
    content: Dict[str, Any]
    cover: Optional[str] = None

class NewsCreate(NewsBase):
    author_id: int

class NewsOut(NewsBase):
    id: int
    published_at: datetime
    author_id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    news_id: int
    author_id: int

class CommentOut(CommentBase):
    id: int
    published_at: datetime
    news_id: int
    author_id: int

    class Config:
        from_attributes = True
        
class CommentUpdate(BaseModel):
    text: Optional[str] = None