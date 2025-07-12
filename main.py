from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()
router = APIRouter(prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
