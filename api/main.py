from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette import status

from .schemas.schemas import Text,Response
from models.model import TextModel,ResponseModel
app = FastAPI()

@app.post("/input/{id}",status_code=status.HTTP_201_CRREATED)
def create(request: Text, db:Session):
    put=TextModel(body=request.body)
    db.add(put)
    db.commit()
    db.refresh(put)
    return put
@app.get("/response",status_code=status.HTTP_200_OK)
def response(response:Response):
    #logic here
    return response
@app.get("/get input/{id}",status_code=status.HTTP_200_OK)
def get_input(id:int,db:Session):
    get=db.query(TextModel).filter(TextModel.id==id).first()
    return get
@app.get("/get_response/{id}",status_code=status.HTTP_200_OK)
def response(id:int,db:Session):
    get=db.query(ResponseModel).filter(TextModel.id==id).first()
    return get