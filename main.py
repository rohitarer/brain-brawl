from fastapi import FastAPI
from routers.categories_router import router as category
from routers.questions_router import router as question

app = FastAPI(title='Brain Brawl API')

app.include_router(category)
app.include_router(question)

@app.get("/health")
def health_check():
    return {
        'status': 'Running',
        'app': 'Brain Brawl'
    }