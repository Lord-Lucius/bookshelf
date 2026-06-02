from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/books", tags=["books"])

books = [
    {"id": 0, "title": "harry potfleur", "description": "basic desc"},
    {"id": 1, "title": "lilo et pitch", "description": "basic desc"},
    {"id": 2, "title": "les mondes de narnic", "description": "basic desc"},
]

@router.get("")
async def get_all_books():
    return books

@router.get("/{book_id}")
async def get_book_by_id(book_id: int):
    for item in books:
        if item["id"] == book_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("")
async def create_book(item: dict):
    for book in books:
        if item["id"] == book["id"] or item["title"] == book["title"]:
            raise HTTPException(status_code=409, detail="item already exists")

    if item["id"] > len(books):
        item["id"] = len(books)
    books.append(item)
    raise HTTPException(status_code=201, detail="item created")
