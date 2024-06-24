from contextlib import asynccontextmanager

from app.db import init_db

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield


app = FastAPI(docs_url="/api/docs", redoc_url=None, lifespan=lifespan)

# app.include_router(root.router, prefix="/api")

origins = [
    "",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
