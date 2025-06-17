from api.routers.chat import router as chat_router
from api.routers.recipe_router import router as recipe_router
from api.routers.ingredient import router as ingredient_router
from fastapi import FastAPI
from api.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, 
              version=settings.PROJECT_VERSION)

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(recipe_router, prefix="/recipes", tags=["recipes"])
app.include_router(ingredient_router, prefix="/ingredients", tags=["ingredients"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)
# Run with: uvicorn api.main:app --reload
# poetry run uvicorn api.main:app --reload