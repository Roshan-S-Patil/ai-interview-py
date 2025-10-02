from fastapi import HTTPException
from models.schema import ChatRequest, ChatResponse
from services.chat_service import handle_chat, handle_chat_async
from fastapi import Depends

# If synchronous style
def chat_handler(req: ChatRequest) -> ChatResponse:
    try:
        out_msgs = handle_chat(req.thread_id, req.messages)
        return ChatResponse(messages=out_msgs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# If you want async handler
async def chat_handler_async(req: ChatRequest) -> ChatResponse:
    try:
        out_msgs = await handle_chat_async(req.thread_id, req.messages)
        return ChatResponse(messages=out_msgs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
