from fastapi import FastAPI

from app.routers import router

app = FastAPI(docs_url="/")
app.include_router(router, tags=["data"])
