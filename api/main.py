from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette import status

from .schemas.schemas import Text,Response

app = FastAPI()

@app.post("/get_text/id",status_code=status.HTTP_201_CRREATED)
def create(request: Text):
    return request
@app.get("/get_response",status_code=status.HTTP_200_OK)
def get_response(response:Response):
    #logic here
    return response