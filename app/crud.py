from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas


class CRUDUser:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
        return db.query(models.User).offset(skip).limit(limit).all()
    
    def get_by_id(self, db: Session, user_id: int) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.id == user_id).first()
    
    def get_by_email(self, db: Session, email: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.email == email).first()
    
    def create(self, db: Session, user: schemas.UserCreate) -> models.User:
        db_user = models.User(
            name=user.name,
            email=user.email,
            is_verified_author=user.is_verified_author,
            avatar=user.avatar
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def update(self, db: Session, user_id: int, user_update: schemas.UserCreate) -> Optional[models.User]:
        db_user = self.get_by_id(db, user_id)
        if db_user:
            for field, value in user_update.dict(exclude_unset=True).items():
                setattr(db_user, field, value)
            db.commit()
            db.refresh(db_user)
        return db_user
    
    def delete(self, db: Session, user_id: int) -> bool:
        db_user = self.get_by_id(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False


class CRUDNews:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.News]:
        return db.query(models.News).offset(skip).limit(limit).all()
    
    def get_by_id(self, db: Session, news_id: int) -> Optional[models.News]:
        return db.query(models.News).filter(models.News.id == news_id).first()
    
    def get_by_author(self, db: Session, author_id: int) -> List[models.News]:
        return db.query(models.News).filter(models.News.author_id == author_id).all()
    
    def create(self, db: Session, news: schemas.NewsCreate) -> models.News:
        # Проверяем, что автор верифицирован
        author = db.query(models.User).filter(models.User.id == news.author_id).first()
        if not author or not author.is_verified_author:
            raise ValueError("Only verified authors can create news")
        
        db_news = models.News(
            title=news.title,
            content=news.content,
            author_id=news.author_id,
            cover=news.cover
        )
        db.add(db_news)
        db.commit()
        db.refresh(db_news)
        return db_news
    
    def update(self, db: Session, news_id: int, news_update: schemas.NewsCreate) -> Optional[models.News]:
        db_news = self.get_by_id(db, news_id)
        if db_news:
            for field, value in news_update.dict(exclude_unset=True).items():
                setattr(db_news, field, value)
            db.commit()
            db.refresh(db_news)
        return db_news
    
    def delete(self, db: Session, news_id: int) -> bool:
        db_news = self.get_by_id(db, news_id)
        if db_news:
            db.delete(db_news)
            db.commit()
            return True
        return False


class CRUDComment:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.Comment]:
        return db.query(models.Comment).offset(skip).limit(limit).all()
    
    def get_by_id(self, db: Session, comment_id: int) -> Optional[models.Comment]:
        return db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    
    def get_by_news(self, db: Session, news_id: int) -> List[models.Comment]:
        return db.query(models.Comment).filter(models.Comment.news_id == news_id).all()
    
    def get_by_author(self, db: Session, author_id: int) -> List[models.Comment]:
        return db.query(models.Comment).filter(models.Comment.author_id == author_id).all()
    
    def create(self, db: Session, comment: schemas.CommentCreate) -> models.Comment:
        db_comment = models.Comment(
            text=comment.text,
            news_id=comment.news_id,
            author_id=comment.author_id
        )
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    
    def update(self, db: Session, comment_id: int, comment_update: schemas.CommentCreate) -> Optional[models.Comment]:
        db_comment = self.get_by_id(db, comment_id)
        if db_comment:
            for field, value in comment_update.dict(exclude_unset=True).items():
                setattr(db_comment, field, value)
            db.commit()
            db.refresh(db_comment)
        return db_comment
    
    def delete(self, db: Session, comment_id: int) -> bool:
        db_comment = self.get_by_id(db, comment_id)
        if db_comment:
            db.delete(db_comment)
            db.commit()
            return True
        return False


user = CRUDUser()
news = CRUDNews()
comment = CRUDComment()
