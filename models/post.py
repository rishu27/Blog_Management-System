from pydantic import BaseModel, Field
class Post(BaseModel):
    title: str = Field(..., description="The title of the blog post")
    content: str = Field(..., description="The content of the blog post")
    author: str = Field(..., description="The author of the blog post")