from fastapi import APIRouter
from app.services.books import get_books_metadata

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)
# Route for fetching Books.
@router.get("/")
def get_books():
    books = get_books_metadata()
    return books
        