from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    registered_at = Column(DateTime, default=datetime.utcnow)
    is_verified_author = Column(Boolean, default=False)
    avatar = Column(String, nullable=True)
    
    # Отношения ВНУТРИ класса
    news = relationship("News", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(JSON, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    cover = Column(String, nullable=True)
    
    # Отношения ВНУТРИ класса
    author = relationship("User", back_populates="news")
    comments = relationship("Comment", back_populates="news", cascade="all, delete")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    news_id = Column(Integer, ForeignKey("news.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    published_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения ВНУТРИ класса
    news = relationship("News", back_populates="comments")
    author = relationship("User", back_populates="comments")