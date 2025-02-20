from fastapi import FastAPI
from views.book_views import books_router


fastapi_app = FastAPI()

fastapi_app.include_router(books_router)



@fastapi_app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
