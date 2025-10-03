from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/news", tags=["news"])

@router.post("/", response_model=schemas.NewsOut)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    # Проверяем, что автор верифицирован
    author = db.query(models.User).filter(models.User.id == news.author_id).first()
    if not author or not author.is_verified_author:
        raise HTTPException(status_code=403, detail="Only verified authors can create news")
    
    db_news = models.News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

@router.get("/", response_model=List[schemas.NewsOut])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = db.query(models.News).offset(skip).limit(limit).all()
    return news

@router.get("/{news_id}", response_model=schemas.NewsOut)
def read_news_item(news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news

@router.put("/{news_id}", response_model=schemas.NewsOut)
def update_news(news_id: int, news_update: schemas.NewsCreate, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    for field, value in news_update.dict().items():
        setattr(news, field, value)
    
    db.commit()
    db.refresh(news)
    return news

@router.delete("/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    db.delete(news)
    db.commit()
    return {"message": "News and all comments deleted"}