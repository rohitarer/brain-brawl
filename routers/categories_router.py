from fastapi import APIRouter, HTTPException
from store import categories
from schemas.categories import CategoryCreate

router = APIRouter(
    prefix= "/categories",
    tags= ["Categories"]
)

@router.get("")
def get_categories():
    return {
        'message': 'Categories',
        'data': categories
    }


@router.post("", status_code=201)
def post_category(category: CategoryCreate):
    if category.name in categories:
        raise HTTPException(
            status_code=409,
            detail="Category already exists"
        )

    categories.append(category.name)
    return {
        'message': 'success',
        'data': categories
    }
