from fastapi import FastAPI, APIRouter
import uvicorn
from http_client import http_client
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    http_client.start()
    yield
    await http_client.stop()


app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
