from pydantic import BaseModel

class text(BaseModel):
    title:str
    body:str
class response(BaseModel):
    body:str