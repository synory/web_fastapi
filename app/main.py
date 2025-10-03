from fastapi import FastAPI
from app.routers import users, news, comments

app = FastAPI(title="News API")

app.include_router(users.router)
app.include_router(news.router)
app.include_router(comments.router)

@app.get("/")
def root():
    return {"message": "News API is running"}