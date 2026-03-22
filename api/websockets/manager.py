# api/websockets/manager.py
from fastapi import WebSocket
from typing import Any, Dict, Union
from pydantic import BaseModel
from schemas.schemas import Text,Response
class ConnectionManager:
    def __init__(self):
        self.active: dict[str, WebSocket] = {}

    async def connect(self, client_id: str, ws: WebSocket):
        await ws.accept()
        self.active[client_id] = ws

    def disconnect(self, client_id: str):
        self.active.pop(client_id, None)

async def send_text(self, client_id: str, data: Text):
    ws = self.active.get(client_id)
    if ws:
        await ws.send_json(data.model_dump())

async def send_response(self, client_id: str, data: Response):
    ws = self.active.get(client_id)
    if ws:
        await ws.send_json(data.model_dump())
manager = ConnectionManager()
