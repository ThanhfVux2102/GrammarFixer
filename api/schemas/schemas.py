from pydantic import BaseModel

class Text(BaseModel):
    request_id:str
    body:str
class Response(BaseModel):
    request_id:str
    body:str