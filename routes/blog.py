from fastapi import APIRouter, HTTPException
from models.post import Post

router = APIRouter()

posts = []

@router.post("/posts/", response_model=Post, summary="Create a new blog post")
def create_post(post: Post):
    """
    Create a new blog post.
    
    - **title**: The title of the post.
    - **content**: The content of the post.
    - **author**: The author of the post.
    """
    posts.append(post)
    return post

@router.get("/posts/", response_model=list[Post], summary="Retrieve all blog posts")
def get_posts():
    """Retrieve a list of all blog posts."""
    return posts

@router.put("/posts/{title}", response_model=Post, summary="Update an existing blog post")
def update_post(title: str, updated_post: Post):
    """
    Update a blog post by its title.
    
    - **title**: The title of the existing post to update.
    - **updated_post**: The updated post data.
    """
    for index, post in enumerate(posts):
        if post.title == title:
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/posts/{title}", summary="Delete a blog post")
def delete_post(title: str):
    """
    Delete a blog post by its title.
    
    - **title**: The title of the post to delete.
    """
    global posts
    posts = [post for post in posts if post.title != title]
    return {"message": "Post deleted successfully"}