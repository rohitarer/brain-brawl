from pydantic import BaseModel, Field


class QuestionsCreate(BaseModel):
    id: int = Field(gt=0)
    category: str = Field(min_length=3, max_length=50)
    question: str = Field(min_length=10)
    options: list[str] = Field(min_length=4, max_length=4)
    correct_index: int = Field(ge=0, le=3)