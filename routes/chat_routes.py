from fastapi import APIRouter
from models.schema import ChatRequest, ChatResponse
from controllers.chat_controller import chat_handler, chat_handler_async

router = APIRouter()

# sync endpoint:
@router.post("/ask", response_model=ChatResponse)
def ask(req: ChatRequest):
    return chat_handler(req)

# async endpoint:
@router.post("/ask-async", response_model=ChatResponse)
async def ask_async(req: ChatRequest):
    return await chat_handler_async(req)
