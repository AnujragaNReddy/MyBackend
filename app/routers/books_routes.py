from fastapi import APIRouter
from app.services.books import get_books_metadata

router = APIRouter()

# Route for fetching Books.
@router.get("/books")
def get_books():
    books = get_books_metadata()
    return books
        