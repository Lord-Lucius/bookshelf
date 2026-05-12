from fastapi import FastAPI

# personalized import
from .routes.status import router as health_status
from .routes.books import router as books_routes

def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "hello world"}

    app.include_router(health_status)
    app.include_router(books_routes)

    return app

app = create_app()
