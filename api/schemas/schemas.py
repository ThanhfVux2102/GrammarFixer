from pydantic import BaseModel

class Text(BaseModel):
    body:str
class Response(BaseModel):
    body:str