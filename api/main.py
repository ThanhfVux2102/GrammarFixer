from fastapi import FastAPI
from models import text
from sqlalchemy.orm import Session
from starlette import status

app = FastAPI()

@app.post("/get_text/",status_code=status.HTTP_201_CRREATED)
