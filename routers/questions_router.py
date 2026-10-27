from fastapi import APIRouter, HTTPException
from store import questions, categories
from schemas.questions import QuestionsCreate


router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


# @router.get("")
# def get_questions():
#     return {
#         "message": "Questions",
#         "data": questions
#     }


@router.post("", status_code=201)
def post_question(question: QuestionsCreate):
    if any(q['id'] == question.id for q in questions):
        print(question.id)
        raise HTTPException(
            status_code=404,
            detail="Question with this id already exists"
        )

    if not any(c.lower() == question.category.lower() for c in categories):
        raise HTTPException(
            status_code=404,
            detail="Category does not exists"
        )

    questions.append(question.model_dump())
    return {
        "message": "success",
        "data": questions
    }


@router.get("/{ques_id}", status_code=200)
def get_byId(ques_id: int):
    for q in questions:
        if q['id'] == ques_id:
            return {
                "message": "question",
                "data": {
                    "id": q["id"],
                    "category": q["category"],
                    "question": q['question'],
                    "options": q['options']
                }
            }
    raise HTTPException(
        status_code=404,
        detail="Question doesn't exist"
    )



@router.get("")
def get_category_questions(category: str | None = None):
    cat_ques=[]
    if category in categories:
        if not questions:
            return "No questins exist"
        for q in questions:
            if q["category"] == category:
                cat_ques.append(q["question"])
        return {
            "message": category,
            "data": cat_ques
        }
    raise HTTPException(
        status_code= 404,
        detail= "Category not found"
    )