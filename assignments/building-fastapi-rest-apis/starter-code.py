from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="School Library API")


class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    publication_year: int = Field(ge=1000, le=2100)


class StoredBook(Book):
    id: int


books: dict[int, StoredBook] = {}
next_id = 1


@app.get("/books")
def get_books() -> list[StoredBook]:
    return list(books.values())
