from fastapi import FastAPI
from routes.blog import router as blog_router

app = FastAPI()

app.include_router(blog_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}