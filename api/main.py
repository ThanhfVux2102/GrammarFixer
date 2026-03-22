from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from starlette import status

from schemas.schemas import Text,Response
from models.model import TextModel,ResponseModel
from database import get_db
app = FastAPI()

@app.post("/input",status_code=status.HTTP_201_CREATED,tags=["request"])
def create(request: Text, db:Session=Depends(get_db)):
    put=TextModel(body=request.body)
    db.add(put)
    db.commit()
    db.refresh(put)
    out_text=f"idk {id}"#xử lý logic ở đây 
    resp=ResponseModel(text_id=put.id,body=out_text)
    db.add(resp)
    db.commit()
    db.refresh(resp)
    return{
        "input":{"id":put.id,"body":put.body},
        "output": {"id":resp.id,"body":resp.body}
    }
@app.get("/get_input/{id}",status_code=status.HTTP_200_OK,tags=["request"])
def get_input(id:int,db:Session=Depends(get_db)):
    get=db.query(TextModel).filter(TextModel.id==id).first()
    return get
@app.get("/get_response/{id}",status_code=status.HTTP_200_OK,tags=["response"])
def response2(id:int,db:Session=Depends(get_db)):
    get=db.query(ResponseModel).filter(ResponseModel.id==id).first()
    return get