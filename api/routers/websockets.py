from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from api.websockets.manager import manager

router = APIRouter()

@router.websocket("/ws/gec/{client_id}")
async def ws_gec(ws: WebSocket, client_id: str):
    await manager.connect(client_id, ws)
    try:
        while True:
            msg = await ws.receive_json()
            await manager.send_json(client_id, {"type": "echo", "data": msg})
    except WebSocketDisconnect:
        manager.disconnect(client_id)
