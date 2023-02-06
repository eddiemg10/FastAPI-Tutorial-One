from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = False, sort: str | None = None):

    if published:
        return {"data": f"{int(limit)} published blogs from DB"}
    else:
        return {"data": f"{int(limit)}  blogs from DB"}


@app.get("/blog/unpublished")
def unpublishedBlogs():
    return {"data": "All unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit=11):
    return {"data": [1, 2, 3, 4, 5]}


class Blog(BaseModel):
    title: str
    body: str
    published: bool | None


@app.post("/blog")
def createBlog(blog: Blog):
    return {"data": f"Blog was created with title as {blog.title}"}
